###################### Function ######################


### Greeter ###

def personne(name):
    for i in gens:    
        print("Bonjour {}".format(i))
        print("Comment vas-tu aujourd'hui {}".format(i))
        print("{}, es-tu sorti hier soir ?\n".format(i))

gens = ["Gregorie", "Jean", "Lorie"]

personne(gens)

### Full Names ###

def full_name(first_name, last_name):
    print("Hello {} {}\n".format(first_name, last_name))

full_name("Soubika", "Bisoo")
full_name("Chris", "Pratt")
full_name("Britney", "Spears")

### Addition Calculator ###

def addition(a, b):
    print("{} + {} = {}".format(a, b, a+b))

addition(1, 2)
addition(3, 4)
addition(5, 6)

### Return Calculator ###

def addition2(a, b):
    return a+b

print(addition2(1,2))

### List Exercice ###

# Introduction List

def affichage(liste_langage):
    for i in langage:
        print("A nice programming language is {}".format(i))

langage = ["python", "c", "java"]

affichage(langage)

# Common List Operations - Ordered Working List
def affichage2(liste_carrière):
    for i in careers :
        print("version original : {}".format(i))
    for i in sorted(careers):
        print("ordre alphabetique : {}".format(i))
    for i in sorted(careers, reverse=True):
        print("ordre inverse alphabetique :{}".format(i))
    for i in reversed(careers):
        print("ordre inversé : {}".format(i))   

careers = ["programmeur", "professeur", "conducteur",
           "medecin", "journaliste", "garagiste"]

affichage2(careers)

# Slicing a List - Alphabet Slices

def slincing(alpha):
    print("Debut : {}".format(alphabet[:3]))
    print("Milieu : {}".format(alphabet[3:6]))
    print("Fin : {}".format(alphabet[7:]))

alphabet = list(map(chr, range(ord('a'), ord('j')+1)))

slincing(alphabet)