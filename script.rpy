# You can place the script of your game in this file.

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
    theyre = "she's"
    themself = "herself"
    their = "her"
    
    They = "She"
    Them  = "Her"
    Theyre = "She's"
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
    image allura_angry = "characters/allura/angry.png"
    image allura_blushing= "characters/allura/blushing.png"
    image allura_happy = "characters/allura/happy.png"
    image allura_nervous = "characters/allura/nervous.png"
    image allura_normal = "characters/allura//normal.png"
    image allura_stubborn = "characters/allura/stubborn.png"
    image allura_unhappy = "characters/allura/unhappy.png"
    image hunk_angry = "characters/hunk/casual/angry.png"
    image hunk_happy = "characters/hunk/casual//happy.png"
    image hunk_nervous ="characters/hunk/casual/nervous.png"
    image hunk_normal = "characters/hunk/casual/normal.png"
    image hunk_sad = "characters/hunk/casual/sad.png"
    image hunk_stubborn = "characters/hunk/casual/stubborn.png"
    image hunk_surprised = "characters/hunk/casual/surprised.png"
    image hunk_gear_angry = "characters/hunk/gear/angry.png"
    image hunk_gear_happy = "characters/hunk/gear/happy.png"
    image hunk_gear_nervous = "characters/hunk/gear/nervous.png"
    image hunk_gear_normal = "characters/hunk/gear/normal.png"
    image hunk_gear_sad = "characters/hunk/gear/sad.png"
    image hunk_gear_stubborn = "characters/hunk/gear/stubborn.png"
    image hunk_gear_surprised = "characters/hunk/gear/surprised.png"
    image keith_angry = "characters/keith/casual/angry.png"
    image keith_blush = "characters/keith/casual/blush.png"
    image keith_confident = "characters/keith/casual/confident.png"
    image keith_happy = "characters/keith/casual/happy.png"
    image keith_hurt = "characters/keith/casual/hurt.png"
    image keith_nervous = "characters/keith/casual/nervous.png"
    image keith_normal = "characters/keith/casual/normal.png"
    image keith_smirk = "characters/keith/casual/smirk.png"
    image keith_stubborn = "characters/keith/casual/stubborn.png"
    image keith_gear_angry = "characters/keith/gear/angry.png"
    image keith_gear_blush = "characters/keith/gear/blush.png"
    image keith_gear_confident = "characters/keith/gear/confident.png"
    image keith_gear_happy = "characters/keith/gear/happy.png"
    image keith_gear_hurt = "characters/keith/gear/hurt.png"
    image keith_gear_nervous = "characters/keith/gear/nervous.png"
    image keith_gear_normal = "characters/keith/gear/normal.png"
    image keith_gear_smirk = "characters/keith/gear/smirk.png"
    image keith_gear_stubborn = "characters/keith/gear/stubborn.png"
    image lance_angry = "characters/lance/casual/angry.png"
    image lance_blush = "characters/lance/casual/blush.png"
    image lance_crying = "characters/lance/casual/crying.png"
    image lance_flirty = "characters/lance/casual/flirty.png"
    image lance_hurt = "characters/lance/casual/hurt.png"
    image lance_laughing = "characters/lance/casual/laughing.png"
    image lance_nervous = "characters/lance/casual/nervous.png"
    image lance_neutral = "characters/lance/casual/neutral.png"
    image lance_smile = "characters/lance/casual/smile.png"
    image lance_stubborn = "characters/lance/casual/stubborn.png"
    image lance_unconcious = "characters/lance/casual/unconcious.png"
    image lance_gear_angry = "characters/lance/gear/angry.png"
    image lance_gear_blush = "characters/lance/gear/blush.png"
    image lance_gear_crying = "characters/lance/gear/crying.png"
    image lance_gear_flirty = "characters/lance/gear/flirty.png"
    image lance_gear_hurt = "characters/lance/gear/hurt.png"
    image lance_gear_laughing = "characters/lance/gear/laughing.png"
    image lance_gear_nervous = "characters/lance/gear/nervous.png"
    image lance_gear_neutral = "characters/lance/gear/neutral.png"
    image lance_gear_smile = "characters/lance/gear/smile.png"
    image lance_gear_stubborn = "characters/lance/gear/stubborn.png"
    image pidge_angry = "characters/pidge/casual/angry.png"
    image pidge_angryCrying = "characters/pidge/casual/angryCrying.png"
    image pidge_blush = "characters/pidge/casual/blush.png"
    image pidge_crying = "characters/pidge/casual/crying.png"
    image pidge_frustrated = "characters/pidge/casual/frustrated.png"
    image pidge_idea = "characters/pidge/casual/idea.png"
    image pidge_nervous = "characters/pidge/casual/nervous.png"
    image pidge_neutral = "characters/pidge/casual/neutral.png"
    image pidge_skeptical = "characters/pidge/casual/skeptical.png"
    image pidge_smile = "characters/pidge/casual/smile.png"
    image pidge_surprised = "characters/pidge/casual/surprised.png"
    image pidge_tired = "characters/pidge/casual/tired.png"
    image pidge_touched = "characters/pidge/casual/touched.png"
    image pidge_unsure = "characters/pidge/casual/unsure.png"
    image pidge_gear_angry = "characters/pidge/gear/angry.png"
    image pidge_gear_angryCrying = "characters/pidge/gear/angryCrying.png"
    image pidge_gear_blush = "characters/pidge/gear/blush.png"
    image pidge_gear_crying = "characters/pidge/gear/crying.png"
    image pidge_gear_frustrated = "characters/pidge/gear/frustrated.png"
    image pidge_gear_idea = "characters/pidge/gear/idea.png"
    image pidge_gear_nervous = "characters/pidge/gear/nervous.png"
    image pidge_gear_neutral = "characters/pidge/gear/neutral.png"
    image pidge_gear_skeptic = "characters/pidge/gear/skeptic.png"
    image pidge_gear_smile = "characters/pidge/gear/smile.png"
    image pidge_gear_surprised = "characters/pidge/gear/surprised.png"
    image pidge_gear_tired = "characters/pidge/gear/tired.png"
    image pidge_gear_touched = "characters/pidge/gear/touched.png"
    image pidge_gear_unsure = "characters/pidge/gear/unsure.png"
    image shiro_angry = "characters/shiro/casual/angry.png"
    image shiro_angryBlush = "characters/shiro/casual/angryBlush.png"
    image shiro_happy = "characters/shiro/casual/happy.png"
    image shiro_happyBlushl = "characters/shiro/casual/happyBlush.png"
    image shiro_nervous = "characters/shiro/casual/nervous.png"
    image shiro_nervousBlush = "characters/shiro/casual/nervousBlush.png"
    image shiro_neutral = "characters/shiro/casual/neutral.png"
    image shiro_neutralBlush = "characters/shiro/casual/neutralBlush.png"
    image shiro_sad = "characters/shiro/casual/sad.png"
    image shiro_sadBlush = "characters/shiro/casual/sadBlush.png"
    image shiro_smile = "characters/shiro/casual/smile.png"
    image shiro_smileBlush = "characters/shiro/casual/smileBlush.png"
    image shiro_stubborn = "characters/shiro/casual/stubborn.png"
    image shiro_stubbornBlush = "characters/shiro/casual/stubbornBlush.png"
    image shiro_surprise = "characters/shiro/casual/suprise.png"
    image shiro_surpriseBlush = "characters/shiro/casual/surpriseBlush.png"

    
    
    
    $ alluraRoute = False
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
    $ Theyre = theyre.capitalize()
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
            $ theyre="she's"
            $ themself = "herself"
            $ their = "her"
            $ isPlural=0
            
        "He/him/his":
            $ they= "he"
            $ them = "him"
            $ theirs="his"
            $ theyre="he's"
            $ themself = "himself"
            $ their = "his"
            $ isPlural=0
            
        "They/them/their":
            $ they = "they"
            $ them = "them"
            $ theirs ="theirs"
            $ theyre="they're"
            $ themself = "theirself"
            $ their = "their"
            $ isPlural = 1
            
        "Other":
            jump otherPronoun
            
    $ They = they.capitalize()
    $ Them = them.capitalize()
    $ Theirs = theirs.capitalize()
    $ Theyre = Theyre.capitalize()
    $ Themself = themself.capitalize()
    $ Their= their.capitalize()
    jump pronounTest


label otherPronoun:
    "Please enter the correct pronoun in the blank"
    $ they = renpy.input("I watched as ___ went to the Lion. (they)")
    $ them = renpy.input("I went to the Lion with ___. (them)")
    $ theirs = renpy.input("That lion is ___. (theirs)")
    $ theyre = renpy.input("I wonder what ___ are doing? (they're)")
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
    with fade
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
    show lance_gear_flirty with dissolve
    Blue"Well, hello there. Name’s Lance. Aren’t you looking beautiful today."
    #*fade in Shiro normal*
    show shiro_neutral at right with dissolve
    Black "That’s enough, Lance. Is this your house?"
    player "Not anymore!"
    Black "We’re very sorry for crushing your home. Hunk, I think you should apologize."
    "The yellow one steps forward."
    #*fade in sad/nervous Hunk*
    hide shiro_neutral with dissolve
    hide lance_gear_flirty with dissolve
    show hunk_gear_sad with dissolve
    hunk "Yeah, I’m sorry for crushing your house. It kind of blends in with the scenery and I didn’t see it in time."
    "You huff, but you can see the sincerity in his face, and decide to forgive him."
    player "Very well. Apology accepted."
    #*happy Hunk*
    hide hunk_gear_sad 
    show hunk_gear_happy
    #*radio crackle SFX*
    unknown "Hello? Paladins? What’s going on, why haven’t you started training?"
    #*fade in Keith*
    hide hunk_gear_happy with dissolve
    show keith_gear_normal with dissolve
    Red "Hunk stepped on a native’s house."
    hunk "Hey!"
    "You tilt your head, confused."
    player "Training?" 
    show lance_gear_neutral at right with dissolve
    lance "It might not look it, but we’re actually all pilots for this super awesome fighting robot doing fighter-robot awesomeness! Saving the universe and all that."
    player "You don’t mean… Voltron?"
    #*fade in Pidge surprised*
    hide lance_gear_neutral with dissolve
    hide keith_gear_normal with dissolve
    show pidge_gear_surprised with dissolve
    Green "Wait, how do you know that name?"
    player "As isolated as I am, word travels fast in the universe. I’ve heard stories of your heroics, but never thought I would see the mighty Voltron in person. This planet has thus far escaped the Galra’s wrath, but I do not know for how much longer I will be safe in this place. I have already seen the inside of Galran prison ships, and I do not intend to see it again."
    Green "Wait, are you implying that you were once a Galra prisoner!?"
    player "Long ago, yes. I was among a group that was exchanged for Galra commanders captured by a resistance. I may be free but I fear the day when the Galra would find me again."
    hide pidge_gear_surprised with dissolve
    show shiro_smile with dissolve
    Black "Well, how about you come along with us?"
    show keith_gear_angry at right with dissolve
    #*Keith surprised or angry*
    Red "Shiro-! We can’t just bring a stranger along, remember what happened with Rolo and Lance getting his Lion stolen?"
    #*angry Lance*
    show lance_gear_angry at left with dissolve
    lance "Hey, we got it back!"
    #*angry Keith*
    Red "You mean {i}I{/i} got it back!"
    hide shiro_smile 
    show shiro_angry with dissolve
    Black "Lance, Keith! That’s enough. Keith, I understand your concerns, but we just destroyed [their] home. The least we can do is give [them] a new one."
    "The one in red, Keith, crosses his arms and mutters to himself."
    #*neutral Pidge*
    hide shiro_angry
    show pidge_gear_neutral with dissolve
    $ verb = ['was','were'][isPlural]
    Green "Besides, if [they] [verb] a prisoner on a Galra ship,[they] may have information on where my dad and brother are."
    keith "I don’t like it but whatever, I guess."
    hide lance_gear_angry with dissolve
    show hunk_gear_sad at left with dissolve
    hunk "Yeah, I do feel bad about destroying your house…"
    hide pidge_gear_neutral with dissolve
    show shiro_smile with dissolve
    shiro "Then it’s settled! Would you like to come with us to our base? It’s not much and the life we lead is dangerous but we would like for you to come stay with us and fight against the Galra."
    menu:
        "Stay on your planet and rebuild your home":
            jump o1c1
        "Go with Shiro and the others":
            jump o1c2
label o1c1:
    player "I appreciate your offer but I have no desire to throw myself into the Galra’s path. I will remain here and rebuild my home."
    #*sad Lance*
    hide hunk_gear_sad with dissolve
    show lance_gear_hurt at left with dissolve
    hide keith_gear_angry with dissolve
    lance "Awwwwww, please come!"
    shiro "Lance, we can’t force them to do what they don’t want to do. If anything, may we at least help rebuild?"
    "Hunk mimes rolling up sleeves and smiles. The other four smile kindly, and part of you feels bad for rejecting their offer."
    player "I wouldn’t mind the help."
    hide shiro_smile
    show shiro_happy 
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
    hide hunk_gear_sad with dissolve
    show lance_gear_smile at left with dissolve
    #*happy Lance* 
    lance "Aw yeah!"
    "He takes your hand in his."
    lance "Welcome to Team Voltron!"
    keith "Lance, stop flirting with the alien. The last time you did, you and Hunk got brain blasted by an octopus and almost eaten by a giant carnivorous ocean worm."
    lance "Hey, I thought we agreed to never mention that again."
    hide shiro_smile with dissolve
    show hunk_gear_normal with dissolve
    hunk "Let’s get back to the Castle of Lions. I wasn’t really looking forward to training today anyway."
    "You all start walking toward the robot lions, and you cast one final look at your ruined shack before following Shiro through the door to your new life."
    #*fade to black*
    scene black with fade

    #Resume standard storyline

    #*fade to main control room in the Castle of Lions (or whatever we want to call it)*
    scene bg_control_room with fade

    "The doors slide open, and you are in awe of the room around you. Standing at what appears to be the helm of this enormous ship is another figure, with long silver hair. At the sound of your entrance, she turns around angrily."
    show allura_angry with dissolve
    #*Angry Allura*
    unknown "Paladins! What have you been doing all this time when -- Who is this?"
    show shiro_neutral at right with dissolve
    shiro "Allura, this is… actually, I don’t know your name. What is it…?"
    
    #[Name and avatar selection, or have selection at beginning and skip this part]

    player "[playername]! My name is [playername]."
    hide allura_angry 
    show allura_normal 
    #*neutral Allura*
    allura "Is this the native whose home Hunk destroyed?"
    show hunk_gear_nervous at left with dissolve
    hunk "Well when you put it like that…"
    shiro "I offered [playername] a place to stay since we destroyed [their] home."
    allura "It’s nice to meet you, [playername]. These are the paladins of Voltron: Shiro, Lance, Keith, Hunk, and Pidge. I am Princess Allura of the planet Altea, and this is my… Coran? Coran, where are you!?"
    #*clattering and bumping SFX*
    unknown "Right here, Princess!"
    "A man with bright orange hair stumbles into view."
    hide hunk_gear_nervous with dissolve
    #*fade in neutral Coran*
    unknown "I was doing some maintenance in the kitchen. Oh, who is this?"
    allura "This is Coran, my advisor and friend. Coran, this is [playername]. They will be staying with us now."
    coran "Glorious! Can always use a couple extra hands around here!"
    "You smile nervously. It is weird to be surrounded by so many people, but you feel strangely at home."
    hide shiro_neutral with dissolve
    show keith_gear_normal at right with dissolve
    keith "Alright, well, since we didn’t get any team training done today, I’m gonna hit the training deck if anyone needs me."
    #fade out Keith
    hide keith_gear_normal with dissolve
    show hunk_gear_normal at left with dissolve 
    hunk "And while Keith does that, I’m gonna whip us up something for lunch."
    coran "Careful there, Hunk! The pipes are still a bit testy…!"
    hide hunk_gear_normal with dissolve
    #fade hunk and coran
    "Lance lets out a satisfied whine as he stretches."
    show lance_gear_neutral at right with dissolve
    lance "Well if we’re not gonna train today, I’m just gonna take a break, kick back and relax with a space lemonade or something. See you guys later."
    #fade out lance
    hide lance_gear_neutral wtih dissolve
    show pidge_gear_neutral at left with dissolve
    pidge "I’ll be in the Green Lion’s hangar if anyone needs me. I want to run some diagnostics on some intercepted Galra transmissions…"
    hide pidge_gear_neutral with dissolve
    #fade out Pidge
    show shiro_neutral at right with dissolve
    shiro "And then there were three. But I think I’m going to go change into something more comfortable. Allura, why don’t you show [playername] around? I know this place was really hard to figure out when we first got here, too."
    allura "That’s a fabulous idea, Shiro!"
    hide shiro_neutral with dissolve
    #fade out Shiro
    allura "Well then, [playername], shall we get going?"
    player "Oh uh… sure."
    allura "Is there anywhere you would like to see first…?"
    menu:
        "I think Keith said something about a training deck?":
            jump o2c1 
        "I’m feeling a little hungry, so how about that kitchen?":
            jump o2c2
        "Where does everyone relax?":
            jump o2c3
        " I’m curious about what a Lion hangar looks like":
            jump o2c4
        "I’m feeling a little tired, so I think I would like to sleep":
            jump o2c5
        "Anywhere is fine, I guess" if alluraRoute:
            jump o2c6
            
            
label o2c1:
    scene bg_training_deck with fade 
    #fade in training deck
    "You and Allura walk through the sliding doors to the training deck. You’re just in time to see Keith, still wearing his armor, dispatch what you assume to be a sparring drone of some kind. Allura begins to clap joyously."
    show allura_normal with dissolve 
    allura "Well done, Keith! I see that your individual training regime is paying off!"
    "For some reason you can’t tear your eyes away as Keith straightens and wipes his arm across his forehead. He releases his hair from its ponytail, the long strands falling against his neck. The sword he is holding shrinks back into a small handheld device with a snap."
    hide allura_normal 
    show allura_normal at right with dissolve 
    show keith_gear_normal with dissolve
    keith "Thanks, Allura. It seems like I’m the only one, though."
    allura "The others have their own strengths. Anyway, I’m just showing [playername] around the castle for a tick, and [they] asked to see the training deck."
    "Keith looks at you, one eyebrow raised in curiosity."
    keith "Can you fight?"
    player "I know enough to defend myself."
    "Keith jerks his thumb over his shoulder, a half smile curling his lips."
    keith "Wanna spar?"
    player "Wait, like right now?"
    keith "It was just a suggestion. The gladiator is just a robot, it’s not like really fighting a thinking, feeling opponent."
    player "Uh..."
    menu:
        "I’ll pass. Thanks though.":
            jump o2p1c1
        "You're on!":
            jump o2p1c2
        "Lose on purpose":
            jump o2p1c3
            
label o2p1c1:
    player "I’ll pass. Thanks though."
    "Keith shrugs."
    hide keith_gear_normal 
    show keith_gear_angry 
    keith "Yeah, I didn’t think you would."
    allura "Keith, I don’t think asking to fight our guest is the best way to show our hospitality…?"
    "Keith narrows his eyes at you."
    keith "To be honest, I don’t really trust you. The last time we tried to help stranded people, one of the Lions was stolen, and it was a pain getting it back. I really think I have a valid excuse for being distrustful."
    player "Please do not misunderstand; I just don’t think I would be able to beat you in a fight."
    keith "That’s just it though. I want to see exactly what you are capable of. But I’m not so immoral that I would attack someone off guard so I’m just gonna drop it."
    hide allura_normal
    show allura_angry at right 
    allura "Keith, don’t be rude!"
    keith "I’m just thinking like a Paladin, Allura. [playername] was a prisoner on a Galra ship, and we don’t know what [theyre] capable of. We have to be cautious. What if [theyre] being mind controlled or something?"
    allura "Keith, you’re being unreasonable."
    "You get the feeling that Keith has a different way of operating than the rest of the paladins. Everyone else struck you as more or less carefree, intelligent beyond compare but also kind and trusting."
    "Keith, on the other hand, emits a strong air of defense, like walls are erected around his heart and can only be torn down with a nail and hammer, chipping away until the soft center is exposed. You can’t help but wonder what kind of experience he had to make him put up such strong walls."
    "Some part of you wants to find out exactly what he’s hiding under that tough exterior."
    player "No, it’s alright. I understand. I was indeed a prisoner, and I have seen the things they do to the others. No prisoner is exempt from the druid experiments. Keith, I hope you can see that I mean you, and the rest of the people on this ship, no harm."
    "Keith eyes you warily, but you see some of the tension release from his shoulders."
    keith "Whatever." 
    hide keith_gear_angry
    hide allura_angry 
    show allura_normal at right
    jump o2c1mp

label o2p1c2:
    "You feel the flames of competition spark in your belly. You feel a need to somehow prove yourself worthy of being on the ship, of joining Team Voltron."
    player "You’re on!"
    hide keith_gear_normal
    show keith_gear_confident 
    "Keith grins confidently."
    keith "Bring it."
    hide allura_normal with dissolve
    "Allura steps back as you follow Keith into the center of the training center."
    hide keith_gear_confident with dissolve
    "You begin to gently spar, throwing punches and jabs, testing out the other’s style. Slowly, your and Keith’s movements speed up until it is almost impossible to tell whose arm belongs to who. It seems you two are evenly matched."
    "Both of your arms begin to tire, but you are determined to win this match. Finally, you see an opening in Keith’s footwork, and strike just so he loses his balance. You pounce, and the match ends with your knees on either side of Keith’s torso, your forearm pressed against his neck and the other pinning Keith’s shoulder to the ground."
    player "*gasp* I win."
    "Keith taps the ground and you let him up. You offer a hand to help him stand, and he takes the offer. The way he’s looking at you is… indecipherable."
    show keith_gear_normal with dissolve
    keith "That’s the first time I’ve been beaten in close combat by something besides a drone."
    menu:
        "I can make it a second time.":
            player "I can make it a second time."
            hide keith_gear_normal
            show keith_gear_confident 
            #surprised keith
            #neutral keith
            keith "Don’t count on it."
            show allura_normal at right with dissolve
            hide keith_gear_confident
            jump o2c1mp
        "I hope I didn't hurt you too badly.":
            player "I hope I didn’t hurt you too badly."
            hide keith_gear_normal
            show keith_gear_confident
            keith "Takes more than that to hurt me. You’re a good fighter, I’ll give you that. It doesn’t mean I trust you, though."
            player "I wouldn’t expect you to. But I thought you would be able to tell if I lost on purpose to make myself look weak."
            "Keith raises his eyebrows, and you think you hear the ghost of a chuckle."
            show allura_normal at right with dissolve
            jump o2c1mp
    
label o2p1c3:
    "You are torn. You don’t want to come off as aggressive and dangerous, but also not as weak or defenseless. You want Keith to trust you. So what if you fight, but lose on purpose?"
    "Keith would think you’re not afraid of a fight but also not strong enough to potentially attack him in his sleep."
    player "Alright, fine. One short match."
    hide allura_normal with dissolve
    "Keith gets a look in his eye that you can’t quite read, and inclines his head toward the center of the arena. You follow."
    hide keith_gear_normal
    show keith_gear_confident
    keith "Give me all you got."
    hide keith_gear_confident with dissolve
    "You raise your fists. The first few blows are tentative. You put half your strength into each strike, and angle your body to reduce damage inflicted from Keith’s, but it still hurts."
    "This continues for another minute, and you are starting to get winded. Then you see what could be the final blow to end the fight; a right handed uppercut. You are in an easy position to block, but it’s high time to end the fight. You brace for impact…"
    keith "Uuaaah!"
    "The blow connects, and you let yourself fall backward, collapsing on the cold floor. The match is over."
    menu:
        "Ow, that hurt.":
            player "Ow, that hurt."
            show keith_gear_normal with dissolve
            "Keith stands over you, his chest heaving, and holds out a hand for you to take."
            keith "I didn’t put near as much strength into that as I could have. It shouldn’t hurt that much."
            player "I guess that just shows how much stronger you are than me. Perhaps you can see me as less of a threat…?"
            hide keith_gear_normal
            show keith_gear_angry
            "Keith’s eyes narrow. Oh no, was that too much?"
            keith "Don’t think this means I trust you all of a sudden."
            player "O-oh, of course."
            "You take his hand and he pulls you to your feet."
            show allura_normal at right with dissolve
            hide keith_gear_angry
            jump o2c1mp
            
        "Wow, you're really strong.":
            player "Wow, you’re really strong."
            show keith_gear_angry with dissolve
            keith "If you’re trying to win my trust through flattery, it won’t work."
            player "That’s not what I intended at all. I was merely trying to compliment your skill."
            hide keith_gear_angry
            show keith_gear_normal
            "Keith still looks disbelieving, but his expression softens slightly. You get the impression that he isn’t complimented like that often. You feel a little guilty for losing on purpose, and wonder whether, if you spar with him again at full strength, who would be the true victor."
            "He holds his hand out for you, and you take it."
            show allura_normal at right with dissolve
            jump o2c1mp
            
label o2c1mp:
    show keith_gear_normal 
    #fade in neutral allura
    allura "Alright, well I think it’s almost time to make our departure. Keith, I think you should start to think about turning in, soon."
    keith "Yeah. I’m gonna hit the showers first, though."
    "Keith moves away to collect the rest of his gear. He walks towards the door, but just before leaving, he turns and looks in your direction. You mean his gaze strongly, and then he’s gone."
    allura "I apologize about Keith. He’s the pilot of the Red Lion so he’s a bit… uncontrollable and hard to read."
    player "I don’t blame him for being suspicious of me. I would be suspicious of anyone if I was in his position."
    allura "Now enough of that! Let’s continue the tour!"
    "You and Allura walk out of the training deck, the doors hissing shut behind you."
    #fade out training room
    scene black with fade
    ###END; Resume standard plotline
            
label o2c2: 
    jump end
label o2c3:
    jump end
label o2c4:
    jump end
label o2c5:
    jump end
label o2c6:
    jump end
   


label end:
    "end"

