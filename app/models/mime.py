import random

def generate_mime(user_input):

    stop = False
    while stop == False:
        usergreet = False
        mimemove = ["[Mine pulls on invisible rope]","[Mime pretends to be trapped in a box]","[Mime acts as though he is walking on a tightrope]","[Mime stuffs his face with invisible food]","[Mime sits on a invisble chair]","[Mime leans against an invisible wall]","[Mime walks in place]","[Mime applies more white paint to his face]","[Mime gives you a surprised look]","[Mime looks at you with confusion]","[Mime lifts up his hands and backs away]","[Mime shrugs his shoulders]","[Mime places his hand on his hip]","[Mime opens his eyes wide]","[Mime aims a invisble gun at you]","[Mime stares far off into the distance]","[Mime holds out his hat for you to put in some change]","[Mime gives you a wide smile]","[Mime does a dramatic dance]","[Mime looks at you pleadingly]","[Mime hands you a flower]" 'pretty',"[Mime hangs himself with an invisible rope]","[Mime climbs a invisible ladder]","[Mime falls to the ground]","[Mime puts on more eyeliner]","[Mime struggles to hold in laughter]","[Mime pretends to drink from a glass]","[Mime pretends to read a newspaper]","[Mime pretends to write a letter]","[Mime pretends to drown]","[Mime licks an invisible ice cream cone]","[Mime pretends to water the plants outside]","[Mime pretends to make a phone call]","[Mime shakes your hand]","[Mime shakes his fists in anger]","[Mime pretends to walk the dog]","[Mime looks like he is starving]","[Mime looks at you annoyed]","[Mime rolls his eyes]","[Mime raises his eyebrows]", "[Mime pretends to cry]"]
        
        greetings = ["Hi","hi","Sup","sup","Hello","hello","evening","afternoon","morning","hey","Hey","up?"]
        partings = ["Bye", "bye", "Goodbye", "goodbye", "See you later", "see you later", "Cya", "cya", "Leaving", "leaving", "Stop", "stop", "STOP"]
        
        
        for opt in greetings:
            if opt in user_input:
                usergreet = True
        for opt in partings:
            if opt in user_input:
                stop = True
        if usergreet == True:
            movement = ("[Mime waves in greeting]")
            stop = True
        elif stop == True:
            movement = ("[Mime waves goodbye and moonwalks away]")
        else:
            movement = random.choice(mimemove)
            stop = True
            
        return movement

def main():
    pass
#     mime(input(">>User:  "))
#     return None

if __name__ == "__main__":
    main()