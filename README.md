# Image Compression with K-Means Clustering

This project is a simple image compression application using the K-Means clustering method. Users can upload an image, choose the number of colors (clusters) for compression, and view/download the compressed image.

## How to Run?

### Locally

1. Clone the repository:
   
    ```bash
    git clone https://github.com/Kunal-Kumar-Sahoo/k-means-compressor.git
    ```

2. Navigate to the project directory:

    ```bash
    cd k-means-compressor/
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the streamlit app:
   
    ```bash
    streamlit run app.py
    ```

5. Access the application in your browser at [http://localhost:8501](http://localhost:8501)


### Using Docker

1. Build the docker image:
   
   ```bash
   docker build -t kmeanscompressor
   ```

2. Run the docker container:

    ```bash
    docker run -p 8501:8501 kmeanscompressor
    ```

3. Access the application in your browser at [http://localhost:8501](http://localhost:8501)


## Project Structure

- `image_compression.py`: Contains the ImageCompression class for handling image compression using K-means clustering.
- `streamlit_app.py`: Defines the StreamlitApp class for the Streamlit web application.

## Requirements

- Python 3.10
- Streamlit
- scikit-learn
- scikit-image
- seaborn
- matplotlib
- Pillow

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the power of image compression algorithms.

Feel free to contribute and open issues if you encounter any problems!
