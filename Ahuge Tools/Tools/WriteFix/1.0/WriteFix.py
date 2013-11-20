def WriteFix():
    scriptName = nuke.root().name()
    length = len(scriptName)
    filmCheck = scriptName[3]
    if length >= 5:
        if str(filmCheck) == "F":
            Task = scriptName[-10]+scriptName[-9]+scriptName[-8]
    
            if str(Task) == "pnt":
                CreateCrop = nuke.createNode("Crop")
                CreateWrite = nuke.createNode("Write")
                CreateWrite['name'].setValue(scriptName[67:-11])

                CreateCrop['crop'].setValue(0)
                CreateWrite['channels'].setValue('rgb')
            elif str(Task) == "rot":
                CreateCrop = nuke.createNode("Crop")
                CreateWrite = nuke.createNode("Write")
    
                CreateCrop['crop'].setValue(0)
                CreateWrite['channels'].setValue('all')    
                CreateWrite['name'].setValue(scriptName[73:-11])
            else:
                nuke.message('Youre script has not been saved or it is named incorrectly\nCheck to make sure that you have your Task set properly')
        
        elif str(filmCheck) == "S":
            Task = scriptName[-10]+scriptName[-9]+scriptName[-8]
    
            if str(Task) == "pnt":
                CreateCrop = nuke.createNode("Crop")
                CreateWrite = nuke.createNode("Write")
    
                CreateCrop['crop'].setValue(0)
                CreateWrite['channels'].setValue('rgb')
                CreateWrite['name'].setValue(scriptName[69:-11])
            elif str(Task) == "rot":
                CreateCrop = nuke.createNode("Crop")
                CreateWrite = nuke.createNode("Write")
    
                CreateCrop['crop'].setValue(0)
                CreateWrite['channels'].setValue('all')    
                CreateWrite['name'].setValue(scriptName[75:-11])
            else:
                nuke.message('Youre script has not been saved or it is named incorrectly\nCheck to make sure that you have your Task set properly')

        
        else:
            nuke.message('Your script has not been saved or it is named incorrectly\nCheck to make sure that you have your Task set properly')
            Task = scriptName[-10]+scriptName[-9]+scriptName[-8]
        
    else:
        nuke.message('Your script has not been saved or it is named incorrectly\nCheck to make sure that you have your Task set properly')
