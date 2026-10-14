class imageProcessing:
	def __init__(self,imageName,extention):
		self.imageName=imageName
		self.extention=extention
class images:
	def __init__(self,imgsInGame,numberOfImg):
		self.imgsInGame=imgsInGame
		self.numberOfImg=numberOfImg
ImagesState=images({},0)
def img(code):
	image=imageProcessing("",".png")
	image.imageName=" ".join(code[1:])
	ImagesState.imgsInGame[ImagesState.numberOfImg]=image.imageName,image.extention
	ImagesState.numberOfImg+=1
	