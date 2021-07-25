# MadLibs #
# ======= #

# Brief: Concatenates user input with a default string
# Concepts Used: String Concatenation

# ----- Welcome Message ----- #

print("\n", "The MadLibs: Choose Your Words Wisely", "\n", "=====================================\n")

# ------ Start of Program ----- #

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Persion: ")

madlib = f'''
Computer Programming is so {adj} !!!
It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person} !
'''

print(madlib)

# ------ End of Program ----- #