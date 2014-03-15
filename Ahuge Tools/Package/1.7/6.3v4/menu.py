import nuke
import Tools

#Knob Defaults
nuke.knobDefault("Root.format", "HD")
nuke.knobDefault("Roto.output", "-rgba.red -rgba.green -rgba.blue rgba.alpha")

#RT Hidden Items
n.addCommand("BetterWrite", "Tools.WriteFix()", "w")
n.addCommand("ErodeBlurImport", "Tools.ErodeBlur()", "e")
n.addCommand("Packer", "Tools.Packer()", "#p")
n.addCommand("ChannelPackerImport", "Tools.Saturation()", "+a")

#RT Menu
nuke.menu("Nodes").addMenu("Ahuge Tools", icon="AhugeTools.png") 
nuke.menu("Nodes").addCommand('Ahuge Tools/Roto Output', 'Ahuge_Tools.RotoOutputNode()', "+o")
nuke.menu("Nodes").addCommand('Ahuge Tools/Paintout', 'Ahuge_Tools.Paintout()', "+p")
nuke.menu("Nodes").addCommand('Ahuge Tools/PointsTo3D', 'Ahuge_Tools.P3D()', "+m")
nuke.menu("Nodes").addCommand('Roto Tools/Current Frame Hold', 'Ahuge_Tools.FrameHoldMe()', "+c")
nuke.menu("Nodes").addCommand('Roto Tools/CreateBackdrop', 'Ahuge_Tools.CreateBackdrop()', "+b")
nuke.menu("Nodes").addCommand('Ahuge Tools/Grain Blur', 'Ahuge_Tools.GrainBlur()')
nuke.menu("Nodes").addCommand('Ahuge Tools/Smudge Tool', 'Ahuge_Tools.SmudgeTool()')