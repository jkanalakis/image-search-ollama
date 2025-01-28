# web-chat-ollama

A web-based image search and question-answering application built with Streamlit, LangChain, and Ollama. This project enables users to upload images, generate concise descriptions, index them for efficient retrieval, and interactively search for images using natural language queries or by providing a similar image.

## Features
- **Image Uploading**: Simple interface to upload one or more images from your local system.
- **Image Description Generation**: Utilizes Ollama’s language models to generate concise, one-sentence descriptions of each uploaded image.
- **Text Splitting**: Uses RecursiveCharacterTextSplitter to split large descriptions into smaller chunks for better indexing and retrieval performance.
- **Vector Store**: Leverages an in-memory vector store to quickly retrieve the most relevant images based on text queries or image similarities.
- **Question-Answering**: Provides concise answers to user queries based on the indexed image descriptions.
	•	Interactive Chat Interfaces:
	•	Image Upload: Upload and index new images.
	•	Image Search: Search for images based on textual descriptions.
	•	Image Reverse Search: Find similar images by uploading a reference image.
	•	Navigation: Seamless navigation between different functionalities using Streamlit’s navigation components.

## Getting Started

Prerequisites

1. **Python 3.8+**
Ensure you have a recent version of Python installed on your machine. You can download it from the official website.

2. **Ollama**
This application relies on Ollama’s language models. Refer to Ollama’s documentation for instructions on how to install and configure it.

3. **Embeddings and Vision Model**
The default model used is llama3.3 for embeddings and llava:34b for image description generation. Ensure these models are set up and accessible to Ollama. You can download the models by running :

	`ollama pull llama3.3`

	`ollama pull llava:34b`


## Installation

1. Clone this repository:

	`git clone https://github.com/jkanalakis/web-chat-ollama.git`


2. Navigate to the project directory:

	`cd web-chat-ollama`


3. Install Python dependencies (example shown with pip):

	`pip install -r requirements.txt`

## Running the Application

1. **Start the Streamlit app**:

	`streamlit run app.py`

2. **Open the interface**: After running the command, Streamlit will provide a local URL (e.g., http://localhost:8501). Open it in your browser.

3. **Navigate Between Pages**: Use the navigation menu to switch between Image Upload, Image Search, and Image Reverse Search functionalities.

## Usage

### Image Upload
1. **Select Images**: Click on the “Choose an image” button to select one or more images (.jpg, .jpeg, .png) from your local system.
	
2. **Upload and Index**: Uploaded images are saved to the image-search/images/ directory. Each image is processed to generate a one-sentence description using Ollama’s language model, which is then indexed in the vector store for efficient retrieval.
	
3. **View Uploaded Images**: After uploading, each image will be displayed with its generated description.

### Image Search

1. **Enter Query**: Type a short description or keywords related to the image you’re searching for in the text input box.

2. **Retrieve Images**: The application searches the vector store for the most relevant images based on the query and displays them along with their descriptions.

### Image Reverse Search

1. **Upload Reference Image**: Click on the “Choose an image” button to upload an image similar to the one you want to find.

2. **Find Similar Images**: The application generates a description for the uploaded reference image and searches the vector store for images with similar descriptions, displaying the most relevant matches.

## Customization

- **Prompt Template**: Edit the PROMPT_TEMPLATE in image_indexer.py to change how the model generates image descriptions.

- **Chunk Size**: Adjust chunk_size and chunk_overlap in the RecursiveCharacterTextSplitter for different description lengths or more fine-grained search.

- **Embeddings and Model**: Swap out the Ollama embeddings or model for other language models, depending on your needs. Update the EMBEDDING_MODEL and DESCRIPTION_MODEL constants in image_indexer.py accordingly.

- **Images Directory**: Change the IMAGES_DIRECTORY in image_indexer.py if you prefer to store images in a different location.

## Contributing

Contributions are welcome! Whether it’s improving the code, adding new features, or fixing bugs, your input is valuable. Please follow these steps to contribute:

1. Fork the Repository

	Click the “Fork” button at the top right of the repository page.

2. Clone Your Fork

	`git clone https://github.com/yourusername/web-chat-ollama.git`


3. Create a New Branch

	`git checkout -b feature/YourFeatureName`

4. Make Your Changes

	Implement your feature or bug fix.

5. Commit Your Changes

	`git commit -m "Add your descriptive commit message"`


6. Push to Your Fork

	`git push origin feature/YourFeatureName`


7. Create a Pull Request

	Navigate to the original repository and click “Compare & pull request”. Provide a clear description of your changes and submit.

## License

This project is open-sourced under the MIT License. Feel free to use and modify this code as per the license terms.

Happy searching, and enjoy discovering insights from your images with Ollama!