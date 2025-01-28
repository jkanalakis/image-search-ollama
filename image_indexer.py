import os
import ollama
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore


class ImageIndexer:
    """
    ImageIndexer handles the uploading, description, indexing, and retrieval of images using Ollama's language models and a vector store.
    """

    # Configuration
    EMBEDDING_MODEL = "llama3.3"
    DESCRIPTION_MODEL = "llava:34b"
    IMAGES_DIRECTORY = 'image-search/images/'

    # Initialize embeddings and vector store
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_store = InMemoryVectorStore(embedding=embeddings)

    # Mappings to associate document IDs with image filenames and document objects
    _document_id_to_image = {}
    _document_id_to_document = {}

    @classmethod
    def upload_image(cls, file) -> str:
        """
        Uploads an image, generates its description, indexes it in the vector store, and maps the document ID to the image and document.

        Args:
            file: A file-like object representing the image to upload.

        Returns:
            str: The unique document ID associated with the uploaded image.
        """
        image_path = cls._save_image(file)
        description = cls._generate_image_description(image_path)
        document = Document(page_content=description)
        document_id = cls.vector_store.add_documents([document])[0]

        # Map the document ID to the image filename and document object
        cls._document_id_to_image[document_id] = file.name
        cls._document_id_to_document[document_id] = document

        return document_id

    @classmethod
    def _save_image(cls, file) -> str:
        """
        Saves the uploaded image to the designated images directory.

        Args:
            file: A file-like object representing the image to save.

        Returns:
            str: The file path where the image is saved.
        """
        # Ensure the images directory exists
        os.makedirs(cls.IMAGES_DIRECTORY, exist_ok=True)

        # Construct the full image path
        image_path = os.path.join(cls.IMAGES_DIRECTORY, file.name)

        # Save the image to the specified path
        with open(image_path, "wb") as f:
            f.write(file.getbuffer())

        return image_path

    @classmethod
    def _generate_image_description(cls, image_path: str) -> str:
        """
        Generates a concise description of the image using Ollama's language model.

        Args:
            image_path (str): The file path of the image to describe.

        Returns:
            str: A one-sentence description of the image.
        """
        response = ollama.chat(
            model=cls.DESCRIPTION_MODEL,
            messages=[
                {
                    'role': 'user',
                    'content': 'Tell me what you see in this picture in only one sentence. Be concise.',
                    'images': [image_path]
                }
            ],
            options={'temperature': 0} #Eliminate randomness for consistency
        )

        return response['message']['content']

    @classmethod
    def retrieve_document_by_query(cls, query: str) -> list:
        """
        Retrieves documents from the vector store that are most similar to the given query.

        Args:
            query (str): The search query.

        Returns:
            list: A list of Document objects that are most relevant to the query.
        """
        return cls.vector_store.similarity_search(query, k=1)

    @classmethod
    def retrieve_documents_by_image(cls, image_file) -> list:
        """
        Retrieves documents based on the description of an uploaded image.

        Args:
            image_file: A file-like object representing the image to search by.

        Returns:
            list: A list of Document objects that are most relevant to the image's description.
        """
        image_path = cls._save_image(image_file)
        description = cls._generate_image_description(image_path)
        return cls.retrieve_document_by_query(description)

    @classmethod
    def get_document_by_id(cls, document_id: str) -> Document:
        """
        Retrieves the Document object associated with a given document ID.

        Args:
            document_id (str): The unique identifier of the document.

        Returns:
            Document: The Document object associated with the ID.
        """
        return cls._document_id_to_document.get(document_id)

    @classmethod
    def get_image_path_by_id(cls, document_id: str) -> str:
        """
        Retrieves the file path of the image associated with a given document ID.

        Args:
            document_id (str): The unique identifier of the document.

        Returns:
            str: The file path of the associated image.
        """
        image_filename = cls._document_id_to_image.get(document_id)
        return os.path.join(cls.IMAGES_DIRECTORY, image_filename) if image_filename else None