from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
lemon = (236, 232, 26)
aquamarine = (110, 206, 178)
yellow = (252, 227, 166)

im = Image.open("sreevs.png")

im #this is an image
img_data = im.getdata() #how to call
img_list_data = list(img_data)  #list is a function
width, height = im.size  #(width,size)  into a tuple

def func(img_list_data):
	final_picture = []
	for pixel in img_list_data:
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2] 
		intensity = red + green + blue

		if (intensity <182):
			final_picture.append(darkBlue)
		elif (182 < intensity < 364):
			final_picture.append(red)
		elif (364 <intensity < 546):
			final_picture.append(lightBlue)
		else :
			final_picture.append(yellow)

	return final_picture



colorized_image = func(img_list_data)
new_image = Image.new(im.mode, im.size)
new_image.putdata(colorized_image)
new_image.show()
new_image.save("output", "jpeg")