﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.


init python:

    #isPlural is 0 when pronouns are singular and 1 when they are plural
    isPlural=0
    #in order: personal, possessive, reflexive and object pronouns (not 100% sure these are the right names but w/e)
    
    they = "she"
    them = "her"
    theirs = "hers"
    themself = "herself"
    their = "her"
    
    They = "She"
    Them  = "Her"
    Theirs = "Hers"
    Themself = "Herself"
    Their = "Her"
    global playername
    
    
init:
    image blue = "backgrounds/blue.png"
    image bg_planet = "backgrounds/PlanetBG.png"
    image bg_bedroom = "backgrounds/bedroom.png"
    image bg_dark_bedroom = "backgrounds/bedroom_dark.png"
    image bg_blue_hangar = "backgrounds/BlueLionHangar.png"
    image bg_control_room = "backgrounds/control_room.png"
    image bg_green_hangar  = "backgrounds/green_lion_hangar.png"
    image bg_green_hangar_dark = "backgrounds/green_lion_hangar_dark.png"
    image bg_hallway = "backgrounds/hallway.png"
    image bg_healing_pods = "backgrounds/healings_pods.png"
    image bg_red_hangar = "backgrounds/RedLionHangar.png"
    image bg_training_deck = "backgrounds/training_deck.png"
    image bg_yellow_hangar = "backgrounds/YellowLionHangar.png"
    
    
    
    
    
    $ playername = "Player"
    define player  = Character("[playername]", color="#000000")
    define unknown = Character("????", color="#000000")
    define hunk = Character("Hunk", color="#000000")
    define pidge = Character("Pidge", color="#000000")
    define keith = Character("Keith", color="#000000")
    define lance = Character("Lance", color="#000000")
    define shiro = Character("Shiro", color="#000000")
    define allura = Character("Allura", color="#000000")
    define coran = Character("Coran", color="#000000")
    define Blue = Character("Blue", color="#000000")
    define Black = Character("Black", color="#000000")
    define Red = Character("Red", color="#000000")
    define Green = Character("Green", color="#000000")
    define All = Character("All", color="#000000")
# The game starts here.
label start:
    scene black
    call screen input_screen
    $ They = they.capitalize()
    $ Them = them.capitalize()
    $ Theirs = theirs.capitalize()
    $ Themself = themself.capitalize()
    $ Their= their.capitalize()
    
    $ renpy.pause()
    jump section1
        
   # jump pronounChoose
    
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
            jump pronounChoose
             
    label pronounTest:

    #the more elegant solution - defines the protag's verb beforehand and just adds the rest
    $ verb1= ['sends','send'][isPlural]
    unknown "[Their] milkshake brings all the boys to the yard.[They] [verb1] them away because [they] worked hard for those milkshakes!"

label section1:
    unknown "Bring Voltron to me, and you will be rewarded."
    unknown "I understand. I won’t let you down. Voltron, and the universe, shall be yours."
    #*fade to black*
    scene black
    #*fade to planet background*
    scene bg_planet
    player "Wow, I caught a big haul! Gonna be a feast tonight!"
    "Suddenly, you hear a sound behind you, and you gasp and take shelter behind a large rock, breathing softly. You swallow and peer around the rock."
    player "*gasp* That’s -- !"
    "Five multicolored robot lions have appeared behind you, looking as though they just landed. They aren’t moving. The yellow one has its foot through the roof of your shack; you can hear the shingles falling from your hiding place."
    player "Did… my house seriously just get crushed by a robot lion?!"
    "You get to your feet just as the largest of the five lions, the black one, lowers its head and opens it’s mouth. The other four lions do the same, and from the mouths walk five Earthling creatures. They all talk with one another, but look harmless enough. The one dressed in black seems to be berating the one in yellow."
    "You begin to get angry; your house was just crushed! You walk from around the rock and begin to approach the Earthlings."
    player "Hey! Over here!"
    "All five look in your direction. The one dressed in blue immediately runs to your side."
    #*flirty Lance image*
    Blue"Well, hello there. Name’s Lance. Aren’t you looking beautiful today."
    #*fade in Shiro normal*
    Black "That’s enough, Lance. Is this your house?"
    player "Not anymore!"
    Black "We’re very sorry for crushing your home. Hunk, I think you should apologize."
    "The yellow one steps forward."
    #*fade in sad/nervous Hunk*
    hunk "Yeah, I’m sorry for crushing your house. It kind of blends in with the scenery and I didn’t see it in time."
    "You huff, but you can see the sincerity in his face, and decide to forgive him."
    player "Very well. Apology accepted."
    #*happy Hunk*
    #*radio crackle SFX*
    unknown "Hello? Paladins? What’s going on, why haven’t you started training?"
    #*fade in Keith*
    Red "Hunk stepped on a native’s house."
    hunk "Hey!"
    "You tilt your head, confused."
    player "Training?"
    lance "It might not look it, but we’re actually all pilots for this super awesome fighting robot doing fighter-robot awesomeness! Saving the universe and all that."
    player "You don’t mean… Voltron?"
    #*fade in Pidge surprised*
    Green "Wait, how do you know that name?"
    player "As isolated as I am, word travels fast in the universe. I’ve heard stories of your heroics, but never thought I would see the mighty Voltron in person. This planet has thus far escaped the Galra’s wrath, but I do not know for how much longer I will be safe in this place. I have already seen the inside of Galran prison ships, and I do not intend to see it again."
    Green "Wait, are you implying that you were once a Galra prisoner!?"
    player "Long ago, yes. I was among a group that was exchanged for Galra commanders captured by a resistance. I may be free but I fear the day when the Galra would find me again."
    Black "Well, how about you come along with us?"
    #*Keith surprised or angry*
    Red "Shiro-! We can’t just bring a stranger along, remember what happened with Rolo and Lance getting his Lion stolen?"
    #*angry Lance*
    lance "Hey, we got it back!"
    #*angry Keith*
    Red "You mean {i}I{/i} got it back!"
    Black "Lance, Keith! That’s enough. Keith, I understand your concerns, but we just destroyed [their] home. The least we can do is give [them] a new one."
    "The one in red, Keith, crosses his arms and mutters to himself."
    #*neutral Pidge*
    $ verb = ['was','were'][isPlural]
    Green "Besides, if [they] [verb] a prisoner on a Galra ship,[they] may have information on where my dad and brother are."
    keith "I don’t like it but whatever, I guess."
    hunk "Yeah, I do feel bad about destroying your house…"
    shiro "Then it’s settled! Would you like to come with us to our base? It’s not much and the life we lead is dangerous but we would like for you to come stay with us and fight against the Galra."
    menu:
        "Stay on your planet and rebuild your home":
            jump o1c1
        "Go with Shiro and the others":
            jump o1c2
label o1c1:
    player "I appreciate your offer but I have no desire to throw myself into the Galra’s path. I will remain here and rebuild my home."
    #*sad Lance*
    lance "Awwwwww, please come!"
    shiro "Lance, we can’t force them to do what they don’t want to do. If anything, may we at least help rebuild?"
    "Hunk mimes rolling up sleeves and smiles. The other four smile kindly, and part of you feels bad for rejecting their offer."
    player "I wouldn’t mind the help."
    #*happy Shiro*
    shiro "Great!"
    "You and the five humans spend the remaining time rebuilding your home until it is even larger than before. When it is time for them to leave, you give them some local produce and invite them to visit."
    shiro "Of course. We wish you the best, and stay safe."
    All "Bye-!"
    "You watch as they all board their lions. The robots all rear their mighty heads and release a deafening roar before taking off and exiting the atmosphere, leaving you behind."
    jump end
    
label o1c2:
    "You think about it long and hard, until finally"
    player "I think it’s time I stop running from the Galra, and fight to keep my freedom. I will go with you!"
    #*happy Lance*
    lance "Aw yeah!"
    "He takes your hand in his."
    lance "Welcome to Team Voltron!"
    keith "Lance, stop flirting with the alien. The last time you did, you and Hunk got brain blasted by an octopus and almost eaten by a giant carnivorous ocean worm."
    lance "Hey, I thought we agreed to never mention that again."
    hunk "Let’s get back to the Castle of Lions. I wasn’t really looking forward to training today anyway."
    "You all start walking toward the robot lions, and you cast one final look at your ruined shack before following Shiro through the door to your new life."
    #*fade to black*

    #Resume standard storyline

    #*fade to main control room in the Castle of Lions (or whatever we want to call it)*

    "The doors slide open, and you are in awe of the room around you. Standing at what appears to be the helm of this enormous ship is another figure, with long silver hair. At the sound of your entrance, she turns around angrily."
    #*Angry Allura*
    unknown "Paladins! What have you been doing all this time when -- Who is this?"
    shiro "Allura, this is… actually, I don’t know your name. What is it…?"
    
    #[Name and avatar selection, or have selection at beginning and skip this part]

    player "[playername]! My name is [playername]."
    #*neutral Allura*
    allura "Is this the native whose home Hunk destroyed?"
    hunk "Well when you put it like that…"
    shiro "I offered [playername] a place to stay since we destroyed [their] home."
    allura "It’s nice to meet you, [playername]. These are the paladins of Voltron: Shiro, Lance, Keith, Hunk, and Pidge. I am Princess Allura of the planet Altea, and this is my… Coran? Coran, where are you!?"
    #*clattering and bumping SFX*
    unknown "Right here, Princess!"
    "A man with bright orange hair stumbles into view."
    #*fade in neutral Coran*
    unknown "I was doing some maintenance in the kitchen. Oh, who is this?"
    allura "This is Coran, my advisor and friend. Coran, this is [playername]. They will be staying with us now."
    coran "Glorious! Can always use a couple extra hands around here!"
    "You smile nervously. It is weird to be surrounded by so many people, but you feel strangely at home."
    keith "Alright, well, since we didn’t get any team training done today, I’m gonna hit the training deck if anyone needs me."
    #fade out Keith
    hunk "And while Keith does that, I’m gonna whip us up something for lunch."
    coran "Careful there, Hunk! The pipes are still a bit testy…!"
    #fade hunk and coran
    "Lance lets out a satisfied whine as he stretches."
    lance "Well if we’re not gonna train today, I’m just gonna take a break, kick back and relax with a space lemonade or something. See you guys later."
    #fade out lance
    pidge "I’ll be in the Green Lion’s hangar if anyone needs me. I want to run some diagnostics on some intercepted Galra transmissions…"
    #fade out Pidge
    shiro "And then there were three. But I think I’m going to go change into something more comfortable. Allura, why don’t you show [playername] around? I know this place was really hard to figure out when we first got here, too."
    allura "That’s a fabulous idea, Shiro!"
    #fade out Shiro
    allura "Well then, [playername], shall we get going?"
    player "Oh uh… sure."
    allura "Is there anywhere you would like to see first…?"
    menu:
        "option1"
        "option2"
label end:
    "end"

