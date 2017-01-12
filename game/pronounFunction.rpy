init python:
    #isPlural is 0 when pronouns are singular and 1 when they are plural
    isPlural=0
    #in order: personal, possessive, reflexive and object pronouns (not 100% sure these are the right names but w/e)
    per_pro= "she"
    pos_pro="hers"
    ref_pro = "Herself"
    obj_pro = "her"
 
    #the function to use verbs refering to the PC in the correct conjugation
    #takes four strings:
    #start = the beginning of the line to the verb
    #sing = the singular form of the verb
    #pl = the plural form of the verb
    #end is the line from the verb on
    #do not put spaces at the end of the strings
    
    def verbReplace(start, sing, pl, end):
        #the function  capitalizes the start string just in case it's a pronoun
        #it creates a sequence of strings, (start, verb, end) then joins them with a space in between 
        #if isPlural=0, the verb returned is singular, if it's 1 the verb is plural
        statement=(start.capitalize(), [sing,pl][isPlural], end)
        return " ".join(statement)