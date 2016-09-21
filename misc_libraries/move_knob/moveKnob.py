###@@### moveKnobs.py
__author__ = "Alex Hughes"
__version__ = "15.05.07"

def move( sel, fromKnobName, toKnobName ):
########################################
#
# @param sel is a node object
# @param fromKnobName is the string name of the knob that you want to move.
# @param toKnobName is the string name of the knob that you want to move fromKnob below
#
########################################
    
    fromKnob = ''
    fromIndex = 0
    toIndex = 0
    
    knobList = sel.allKnobs()
    
    index = 0
    for knob in knobList:
        if knob.name() == fromKnobName:
            # Found our fromKnob
            fromKnob = knob
            fromIndex = index
        elif knob.name() == toKnobName:
            toIndex = index
            
        index += 1

    if fromIndex < toIndex:
        lIndex = fromIndex
    else:
        lIndex = toIndex

    knobList.pop( fromIndex )
    knobList.insert( toIndex, fromKnob )
    
    removeKnobs = knobList[lIndex:]
    print removeKnobs    

    for i in removeKnobs:
        sel.removeKnob( i )

    for i in removeKnobs:
        sel.addKnob( i )
