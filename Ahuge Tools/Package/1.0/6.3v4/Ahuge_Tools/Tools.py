import os
import os.path
import shutil
import nuke
def WriteFix():
	CreateCrop = nuke.createNode("Crop")
	CreateWrite = nuke.createNode("Write")
	CreateCrop['crop'].setValue(0)

def GrainBlur():
	nuke.loadToolset("Ahuge_Tools/GrainBlur.nk")
			
def FrameHoldMe():
	FrameHold = nuke.createNode('FrameHold')
	FrameHold['first_frame'].setExpression('root.frame()')
	nuke.selectedNode()['first_frame'].clearAnimated()
	
def P3D():
	nuke.loadToolset("Ahuge_Tools/PointsTo3D.nk"	)
	
def RotoOutputNode():
    #Creates a NoOp
    Placeholder = nuke.createNode("NoOp")
    #assigns a varriable to the currently selected node
    OpNo = nuke.selectedNode()
    #Creates a roto node
    Roto = nuke.createNode("Roto")
    #Creates the RotoOutput tool
    Output = nuke.loadToolset("Ahuge_Tools/Roto_Output_Latest.nk")
    #Sets the first input of the RotoOutput to our NoOp
    Output.setInput (0, Placeholder)
    #Sets the second input to the roto node
    Output.setInput(1, Roto)
	#Move the Output Node
    Output.setXpos (Output.xpos() -140)
    Output.setYpos (Output.ypos() +84)
    #Move the Roto Node
    Roto.setXpos (Output.xpos() -220)
    Roto.setYpos (Output.ypos() +6)
    #Creates a Input node for the roto to connect to
    Dummy = nuke.createNode("Input")
    Roto.setInput(0, Dummy)
    #Deletes the Input and the NoOp
    nuke.delete(Dummy)
    nuke.delete(Placeholder)

def ErodeBlur():
	nuke.loadToolset("Ahuge_Tools/ErodeBlur.nk")

def Packer():
	nuke.loadToolset("Ahuge_Tools/Packer.nk")

def Saturation():
	nuke.loadToolset("Ahuge_Tools/Saturation.nk")
	
def Paintout():
	nuke.loadToolset("Ahuge_Tools/Paintout.nk")