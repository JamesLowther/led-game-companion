from PIL import Image

def randomize(matrix):
    image = Image.new("RGB", matrix.dimensions, color="blue")
    matrix.set_image(image)
