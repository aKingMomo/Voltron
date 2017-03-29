init python:
    class InputValue(object):
        def __init__(self, PC):
            self.PC = PC
           
        def get_text(self):
            return (self.PC)
            
        def set_text(self, s):
            global PC
            PC = s
            return (s)
    class VariableInputValue(InputValue):
        def get_name():
            PC.get_text()
            return(PC)
        def PC (self):
            return (self.PC)

    def shePronoun():
         global they 
         they = "she"
         global them 
         them = "her"
         global theirs
         theirs = "hers"
         global themself
         themself = "herself"
         global their
         their = "her"
         global isPlural
         isPlural = 0
         return (they, them, theirs, themself, their, isPlural)
    def hePronoun():
         global they
         they = "he"
         global them
         them = "him"
         global theirs
         theirs = "his"
         global themself
         themself = "himself"
         global their
         their = "his"
         global isPlural
         isPlural = 0
         return (they, them, theirs, themself, their, isPlural)
    def theyPronoun():
        global they
        they = "they"
        global them
        them = "them"
        global theirs
        theirs="theirs"
        global themself
        themself = "theirself"
        global their
        their = "their"
        global isPlural
        isPlural = 1
        return (they, them, theirs, themself, their,isPlural)

screen input_screen:
    add 'blue'
    add 'white' xalign 0.95 yalign 0.5
    default space = 50
    vbox pos (675,56):
        hbox:
            text "Name: " 
            input value
           
            
            null height space    
        hbox:
            text "Pronouns: "
        vbox:
            null height space
            # textbutton "She/her/hers":
                # action shePronoun
            button  action shePronoun:
                add 'she'
               
        vbox:
            null height space
            # textbutton "He/him/his":
                # action hePronoun
            button action hePronoun:
                add 'he'
                
        vbox:
            null height space
            # textbutton  "They/them/their":
                # action theyPronoun
            button action theyPronoun:
                add 'they'
                
    vbox pos (675, 400):
        textbutton "Done":
            action Return('done')

