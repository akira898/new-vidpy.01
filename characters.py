from check1 import commands
class characters:
	def __init__(self,characters,charName,numberOfChara,alias, aliases):
		self.characters=characters
		self.charName=charName
		self.alias=alias
		self.numberOfChara=numberOfChara
		self.aliases=aliases
charaInfo=characters({},"",0,"",[])
def character(code):
	charaInfo.charName=code[1]
	charaInfo.alias=code[3]
	charaInfo.characters[charaInfo.numberOfChara]=charaInfo.charName,charaInfo.alias
	commands.append(charaInfo.alias+":")
	print(commands)
	charaInfo.aliases.append(charaInfo.alias+":")
	charaInfo.numberOfChara+=1
	