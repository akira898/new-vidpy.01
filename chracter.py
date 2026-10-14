from check1 import commands
#characters no maneja uno solo sinobtodi
class characters:
	def __init__(self,characters,charName,numberOfChara,alias, aliases):
		#nombres de los personajes creados
		self.characters=characters
		#nombre del personaje que se esta procesando
		self.charName=charName
		#alias del personaje que se esta procesando
		self.alias=alias
		#numero de personajes creados
		self.numberOfChara=numberOfChara
		#aliases creados
		self.aliases=aliases
charaInfo=characters({},"",0,"",[])
def character(code):
	charaInfo.charName=code[1]
	charaInfo.alias=code[3]
	charaInfo.characters[charaInfo.numberOfChara]=charaInfo.charName,charaInfo.alias
	commands.append(charaInfo.alias+":")
	print(charaInfo.characters)
	print(commands)
	charaInfo.aliases.append(charaInfo.alias+":")
	charaInfo.numberOfChara+=1
	