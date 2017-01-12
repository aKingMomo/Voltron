# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.



init:
    define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    jump pronounTest
label pronounTest:

    #It seems you can't use a method in a script line, just basic variables, so I did this
    #this is an example of how we can use proper verb and pronoun forms for pulral and singular pronouns
    
    $ line=verbReplace(per_pro, 'is', 'are', 'eating lunch.')
    e '[line]'


