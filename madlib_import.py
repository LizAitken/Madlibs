import madlibGen

want_to_write_madlib = "yes"

def caps(i):
    return i.capitalize() 

while (want_to_write_madlib == "yes"):      
    gender = input("Gender: ")
    your_name = input("Your name: ")
    pronoun = input("Pronoun of gender: ") 
    item_one = input("Magical item: ")
    item_two = input("Magical item: ")
    color = input("Color: ")
    animal = input("Magical animal: ")
    pet_name = input("Name: ")
    flavor = input("Flavor: ")
    new_pronoun = caps(pronoun)
    new_name = caps(your_name)

    print(madlibGen.madlibs(gender, new_name, item_one, item_two, color, animal, pet_name, flavor, new_pronoun))
    
    want_to_write_madlib = input("Would you like to play again?")


