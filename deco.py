def decor(func):
	def inner(name):
		if name=="Sunny":
			print("Hello Sunny Bad Morning")
		else:
			func(name)
	return inner
#calling of the decorator func
@decor
def wish(name):
	print("Hello",name,"Good Morning")

	wish("Azim")
	wish("Hari")
	wish("Sunny")
	
