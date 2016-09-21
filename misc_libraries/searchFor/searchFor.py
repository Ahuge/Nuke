
__author__ = 'ahughes'
import nuke
def getExp( knob ):

    if knob.hasExpression():
        return knob.toScript().replace('{"\\', "").replace('"}', "").replace("_", " ").lower()

def checkFor( searchString ):
    searchString = searchString.replace("_", " " ).lower()
    nodes = []
    for node in nuke.allNodes():
        knobs = node.allKnobs()
        for knob in knobs:
            try:
                if searchString in getExp( knob ):
                    nodes.append( node )
            except:
                try:
                    if searchString in knob.value():
                        nodes.append( node )
                except:
                    pass
        if searchString in node.Class().replace("_", " " ).lower() and node not in nodes:
            nodes.append( node )
        if searchString in node.name().replace("_", " " ).lower() and node not in nodes:
            nodes.append( node )

    if len(nodes):
    
        if (len(nodes) -1):
            manyNodes = "There are " + str(len(nodes)) + " node" + "s that have \"" + searchString + "\" in it. They are:"
        else:
            manyNodes = "There is " + str(len(nodes)) + " node" + " that has \"" + searchString + "\" in it. It is:"
        for i in nodes:
            i['selected'].setValue(True)
            manyNodes += ( "\n" + i.name() )
    
        nuke.message(manyNodes)

    print "done"
    
    
def searchFor():
	checkFor( nuke.getInput("Search String?") )
