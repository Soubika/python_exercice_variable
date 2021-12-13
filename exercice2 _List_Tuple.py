###################### List and Tuple ######################

### Introducing list ###

# Introducing list - First  List
langage = ["python", "c", "java"]
print(langage[0])
print(langage[1])
print(langage[-1])

# Introducing list - First Neast List
langage = ["python", "c", "java"]
print("A nice programming language is " + langage[0])
print("A nice programming language is " + langage[1])
print("A nice programming language is " + langage[-1])

# Introducing list - Your First List
couleurs = ["rouge", "bleu", "rose", "jaune", "violet", "vert"]
for couleur in couleurs:
    print("c'est une belle couleur le : {}".format(couleur))
    

### Lists and Looping ###

# Lists and Looping - First List - Loop
langages = ["python", "c", "java"]
for langage in langages :
    print(langage)


# Lists and Looping - First Neat List - Loop
langages = ["python", "c", "java"]
for langage in langages :
    print("A nice programming language is " + langage)


# Lists and Looping - Your First List - Loop
couleurs = ["rouge", "bleu", "rose", "jaune", "violet", "vert"]
for couleur in couleurs:
    print("Le {} est une belle couleur".format(couleur))


### Common List Operations ###

# Common List Operations - Working List
careers = ["programmeur", "professeur", "conducteur", "medecin"]

for i,e in enumerate(careers):
    index = str(i)
    print(index)

print("programmeur" in careers)

careers.append("journaliste")
careers.insert(2, "garagiste")

for carriere in careers :
    print(carriere)

# Common List Operations - Starting From Empty

carrers = []
careers.append("programmeur")
careers.append("professeur")
careers.append("conducteur")
careers.append("medecin")
careers.append("journaliste")
careers.append("garagiste")

print("programmeur" in careers[0])
print("garagiste" in careers[-1])

# Common List Operations - Ordered Working List
careers = ["programmeur", "professeur", "conducteur",
           "medecin", "journaliste", "garagiste"]

for i in careers:
    print("original order : " + i)

for i in sorted(careers):
    print("alphabetical order : " + i)

for i in careers:
    print("original order : " + i)

for i in sorted(careers, reverse=True):
    print("reverse alphabetical order : " + i)

for i in careers:
    print("original order : " + i)

for i in reversed(careers):
    print("reversed order : " + i)

for i in careers:
    print("original order : " + i)

careers.sort()
for i in careers:
    print("permanently alphabetical order : " + i)
    
careers.sort(reverse=True)
for i in careers:
    print("permanently reverse alphabetical order : " + i)

# Common List Operations - Ordered Number

import random

liste = []

random.seed(0)
i = 0
while i < 5 :
    liste.append(random.randint(0,100))
    i = i + 1

for i in liste :
    lol = str(i)
    print("original Order : " + lol)

for i in sorted(liste) :
    lol = str(i)
    print("increasing Order : " + lol)
    
for i in liste :
    lol = str(i)
    print("original Order : " + lol)
    
for i in sorted(liste, reverse=True) :
    lol = str(i)
    print("decreasing Order : " + lol)
    
for i in liste :
    lol = str(i)
    print("original Order : " + lol)

for i in reversed(liste):
    lol = str(i)
    print("reverse order : " + lol)
    
for i in liste :
    lol = str(i)
    print("original Order : " + lol)

liste.sort()
for i in liste:
    lol = str(i)
    print("permanently increasing order : " + lol)
    
liste.sort(reverse=True)
for i in liste:
    lol = str(i)
    print("permanently decreasing order : " + lol)

# Common List Operations - List Lengths

print(len(liste))
print(len(careers))

### Removing Item from a List ###

famous = ["chris pratt", "britney spears", 
"michael jackson", "Teheiura Teahui"]


del famous[0]
famous.remove("michael jackson")

last_famous = famous.pop()
first_famous = famous.pop(0)

print(famous)

### Slicing a List ###

# Slicing a List - Alphabet Slices

alphabet = list(map(chr, range(ord('a'), ord('j')+1)))

first_batch = alphabet[:3]
middle_batch = alphabet[3:6]
end_batch = alphabet[6:]

print(first_batch)
print(middle_batch)
print(end_batch)

# Slicing a List - Protected List

nom = ["Marie", "Jeanne", "Dimitri"]

copie_nom = nom[:]
copie_nom.append("Jean")
copie_nom.append("Marc")


for i in nom:
    print("Liste des noms orignal : " + i)
    
for i in copie_nom:
    print("Liste des noms copiée : " + i)

### Numerical Lists ###

# Numerical Lists - First Twenty

print(list(range(1,20)))

# Numerical Lists - Larger Sets

print(list(range(1,int(1e6))))

# Numerical Lists - Five Wallets

import random

argent = []

random.seed(0)
i = 0
while i < 5 :
    argent.append(random.randint(0,500))
    i = i + 1
    
print("The fattest wallet has {}$ value in it".format(max(argent)))
print("The skinniest wallet has {}$ value in it".format(min(argent)))
print("All together, these wallets have {}$ value in them".format(sum(argent)))

### List Comprehensions ###

# List Comprehensions - Multiples of Ten

number = []

for i in range(1,11):
    number.append(i*10)

for i in number:
    print(i)

# List Comprehensions - Cubes

number = [i**3 for i in range(1,11)]

for i in number:
    print(i)


# List Comprehensions - Awesomeness





# List Comprehensions - Working Backwards


### Strings as Lists ###

### Tuples ###
### Coding Styles: PEP 8 ###
### Overall Challenges ###
