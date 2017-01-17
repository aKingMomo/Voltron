# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.


init python:

    #isPlural is 0 when pronouns are singular and 1 when they are plural
    isPlural=0
    #in order: personal, possessive, reflexive and object pronouns (not 100% sure these are the right names but w/e)
    
    they = ""
    them = ""
    theirs = ""
    themself = ""
    their = ""
    
    They = ""
    Them  = ""
    Theirs = ""
    Themself = ""
    Their = ""
init:
    define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    jump pronounChoose
    
label pronounChoose:
    menu:
        "Please select your pronouns:"
        
        "She/her/hers":
            $ they= "she"
            $ them = "her"
            $ theirs="hers"
            $ themself = "herself"
            $ their = "her"
            $ isPlural=0
            
        "He/him/his":
            $ they= "he"
            $ them = "him"
            $ theirs="his"
            $ themself = "himself"
            $ their = "his"
            $ isPlural=0
            
        "They/them/their":
            $ they = "they"
            $ them = "them"
            $ theirs ="theirs"
            $ themself = "theirself"
            $ their = "their"
            $ isPlural = 1
            
        "Other":
            jump otherPronoun
            
    $ They = they.capitalize()
    $ Them = them.capitalize()
    $ Theirs = theirs.capitalize()
    $ Themself = themself.capitalize()
    $ Their= their.capitalize()
    jump pronounTest


label otherPronoun:
    "Please enter the correct pronoun in the blank"
    $ they = renpy.input("I watched as ___ went to the Lion. (they)")
    $ them = renpy.input("I went to the Lion with ___. (them)")
    $ theirs = renpy.input("That lion is ___. (theirs)")
    $ themself =  renpy.input("I can't believe [they] piloted the lion all by ___! (themself)")
    $ their =  renpy.input("I got in ___ lion. (their)")
    menu:
        "Which is correct?"
        
        "I can't believe how well [they] FLIES [their] lion":
            $ isPlural=0
            
        "I can't believe how well [they] FLY [their] lion":
            $ isPlural=1
            
        "Neither.":
                jump otherPronoun
                
    $ They = they.capitalize()
    $ Them = them.capitalize()
    $ Theirs = theirs.capitalize()
    $ Themself = themself.capitalize()
    $ Their= their.capitalize()
    menu: 
        "Your pronouns are [they]/[them]/[theirs]?"
        
        "Yes":
            jump pronounTest
            
        "No":
            jump PronounChoose
             
    label pronounTest:

    #the more elegant solution - defines the protag's verb beforehand and just adds the rest
    $ verb1= ['sends','send'][isPlural]
    e "[Their] milkshake brings all the boys to the yard.[They] [verb1] them away because [they] worked hard for those milkshakes!"


