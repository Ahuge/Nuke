def WriteFix():
	CreateCrop = nuke.createNode("Crop")
	CreateWrite = nuke.createNode("Write")
	CreateCrop['crop'].setValue(0)