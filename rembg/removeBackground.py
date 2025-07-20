from rembg import remove

input_path = "image.jpg"
output_path = "result.png"

with open(input_path, "rb") as image_file:
    with open(output_path, "wb") as output_file:
        input_image = image_file.read()
        output_image = remove(input_image)
        output_file.write(output_image)
