print("fgf")
from dialogues import speach
dialoguePosition=0
class text:
	def __init__(self,dialoguePosition,DialogueIn):
		self.dialoguePosition=dialoguePosition
		self.DialogueIn=DialogueIn
TextIn=text(0,speach.dialogues[dialoguePosition][0])
