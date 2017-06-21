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
            
    def name_func(newname):
        store.playername = newname
        
    def shePronoun():
        store.they = "she"
        store.them = "her"
        store.theirs = "hers"
        store.theyre = "she's"
        store.themself = "herself"
        store. their = "her"
        store.isPlural = 0
        return 
         #(they, them, theirs, themself, their, isPlural)
    def hePronoun():
         store.they = "he"
         store.them = "him"
         store.theirs = "his"
         store.theyre = "he's"
         store.themself = "himself"
         store.their = "his"
         store.isPlural = 0
         return 
         #(they, them, theirs, themself, their, isPlural)
    def theyPronoun():
        store.they = "they"
        store.them = "them"
        store.theirs="theirs"
        store.theyre = "they're"
        store.themself = "theirself"
        store.their = "their"
        store.isPlural = 1
        return 
        #(they, them, theirs, themself, their,isPlural)

screen input_screen():
    add 'blue'
    add 'white' xalign 0.95 yalign 0.5
    default space = 50
    vbox pos (675,56):
        hbox:
            text "Name: " 
            button:
                id "name_input1"
                xysize (250, 25)
                action NullAction()
                add Input( default = playername, changed=name_func, button=renpy.get_widget("input_screen","name_input1"))
                   
            null height space    
        hbox:
            text "Pronouns: "
        vbox:
            textbutton "She/her/hers":
                action shePronoun
            #textbutton _("She/her/hers") action shePronoun()
                
               
        vbox:
            textbutton "He/him/his":
                action hePronoun
            #textbutton _("He/him/his") action hePronoun()
                
                
        vbox:
            textbutton  "They/them/theirs":
                action theyPronoun
            #textbutton _("They/them/theirs") action theyPronoun()
                
                
    vbox pos (675, 400):
        null height space
        textbutton "Done":
            action Return('done')

