import random
def autoBackdropCustom():
  # Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.
  '''
  Automatically puts a backdrop behind the selected nodes.
  
  The backdrop will be just big enough to fit all the select nodes in, with room
  at the top for some text in a large font.
  '''
  selNodes = nuke.selectedNodes()
  if not selNodes:
    return nuke.nodes.BackdropNode()

  # Calculate bounds for the backdrop node.
  bdX = min([node.xpos() for node in selNodes])
  bdY = min([node.ypos() for node in selNodes])
  bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
  bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY
  
  # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
  left, top, right, bottom = (-10, -80, 10, 10)
  bdX += left
  bdY += top
  bdW += (right - left)
  bdH += (bottom - top)
  
  n = nuke.nodes.BackdropNode(xpos = bdX,
                              bdwidth = bdW,
                              ypos = bdY,
                              bdheight = bdH,
                              tile_color = int((random.random()*(16 - 10))) + 10,
                              note_font_size=42)
	'''Code Above is written by The Foundry'''
  n['selected'].setValue(True)
  return n

def CreateBackdrop():
	import random
	for i in nuke.selectedNodes():
		if i.Class() == "BackdropNode":
			fColour = [random.random(), random.random(), random.random(), random.random()]
			hColour = int('%02x%02x%02x%02x' % (fColour[0]*255,fColour[1]*255,fColour[2]*255,fColour[3]),16) 
			i['tile_color'].setValue(hColour)
			break
		else:
				FaceBook = nuke.getInput('Name?')
				autoBackdropCustom()
				nuke.selectedNode()['label'].setValue(FaceBook)
				break