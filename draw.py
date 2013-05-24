import Image, ImageDraw

imgsz = 1000
offset = 100

def drawmatrix(matrix):
    recsz = (imgsz - offset * 2) / len(matrix)
    image = Image.new("RGB", (imgsz, imgsz), "white")
    draw = ImageDraw.Draw(image)
    for i in range(len(matrix)):
	for j in range(len(matrix)):
	    left = offset + i * recsz
	    up = offset + j * recsz
	    right = left + recsz
	    down = up + recsz
	    if matrix[i][j] == 0:
		color = "white"
	    else:
		color = "black"
	    draw.rectangle((left, up, right, down), fill = color)
    image.save("newqrcode.png", "PNG")
    return 0

