from sklearn.cluster import MiniBatchKMeans

class ImageCompressor:
    def __init__(self, num_colors=16):
        self.__num_colors = num_colors
        self.__kmeans = MiniBatchKMeans(self.__num_colors)
        self.__flat_images = None

    def __normalize(self, image):
        return image / 255

    def __flatten(self, image):
        return image.reshape(-1, image.shape[-1])
    
    def compress_image(self, image):
        self.__flat_image = self.__flatten(self.__normalize(image))
        self.__kmeans.fit(self.__flat_image)
        new_colors = self.__kmeans.cluster_centers_[self.__kmeans.predict(self.__flat_image)]
        image_recolored = new_colors.reshape(image.shape)

        return image_recolored