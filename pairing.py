#Create list of possible values (one for each student)
#Each character 0-f represents 1-16 in hexadecimal
l = list("0123456789abcdef")
students = ['Jonathan Shaw','Todd Briley','Aaron White','Amos Gichero','Huiqi Zhou','Calder Marshall','Debra Mae Lee','Andreea Uta','Julie Dyer','Justin Uzoije','James Marion','Carl Severe','Ning Yuan','Steven Rodriguez','Blake Bagwell','Ian Price']

#Create set of invalid pairs for error catching
pair_errors = []
for i in range(len(l)):
    pair_errors.append([l[i],l[i]])

#Loop through sets and create all possible combinations
combos = []
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        combos.append([l[i],l[j]])

#Check to see if any duplicates exist in list
for i in combos:
    if combos.count(i) > 1:
        print ERROR

#Create unique sets of pairs
sets = []
used = []
for i in range(len(l)-1):
    s = []
    unique = []
    for j in range(8):
        for k in combos:
            if (k[0] in unique) == False and (k[1] in unique) == False and (k in used) == False:
                s.append(k)
                used.append(k)
                for x in k:
                    unique.append(x)
    sets.append(s)

#Ask which set the user would like to use, then print it
print """
There are 15 possible sets made up of 8 unique pairs each.
Which one would you like to use?
Please enter an integer between 1 and 15, inclusive.\n
"""
response = int(raw_input("Set #"))

pair_set = sets[response-1]
name_pairs = []

for i in pair_set:
    t = []
    for j in i:
        t.append(students[l.index(j)])
    name_pairs.append(t)
    print t
