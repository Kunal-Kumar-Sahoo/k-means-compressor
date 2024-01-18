import numpy as np
import streamlit as st
from skimage.io import imread
from PIL import Image as Image
from image_compression import ImageCompressor
import base64

from warnings import filterwarnings

class WebApp:
    def __init__(self):
        st.title('Image Compression using K-Means Clustering')
        self.__compressor = None
        filterwarnings('ignore')

    def upload_and_compress(self):
        __uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
        if __uploaded_file is not None:
            Image = imread(__uploaded_file)

            st.image(Image, caption='Original Image', use_column_width=True)
            __num_colors = st.slider('Select the number of colors:', 2, 256, 16)
            self.__compressor = ImageCompressor(__num_colors)
            __compressed_image = self.__compressor.compress_image(Image)
            st.image(__compressed_image, caption='Compressed Image', use_column_width=True)
    

def main():
    app = WebApp()
    app.upload_and_compress()


if __name__ == '__main__':
    main()