import os.path

#Open record file
filename = "saved_pairs.txt"
contents = []
if os.path.isfile(filename):
    target = open(filename, 'r+')
    c = list(target.read())
    next_num = ""
    for i in c:
        if i != "\n":
            if i == ",":
                contents.append(int(next_num))
                next_num = ""
            else:
                next_num += i
else:
    target = open(filename, 'w+')
    for i in range(15):
        contents.append(0)
contents_backup = contents

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
print "There are 15 possible sets made up of 8 unique pairs each."
for i in range(len(contents)):
    print "Set #%d has been used %d times." % (i,contents[i])

print """
Which one would you like to use?
Please enter an integer between 1 and 15, inclusive.\n
"""
response1 = int(raw_input("Set #"))

contents[response1 - 1] += 1
pair_set = sets[response1 - 1]
name_pairs = []

for i in pair_set:
    t = []
    for j in i:
        t.append(students[l.index(j)])
    name_pairs.append(t)
    print t

print "Are you done using the program?"
response2 = str(raw_input("(y/n):"))
output_string = ""
response2 ="y"
if response2 == "y":
    print "Do you want to save the records of how many times each set has been used?"
    response3 = str(raw_input("(y/n):"))
    if response3 == "y":
        for i in contents:
            output_string += str(i) + ","
    elif response3 == "n":
        print "Do you want to reset the number of times each set has been used?"
        response4 = str(raw_input("(y/n):"))
        if response4 == "y":
            print "Resetting number of times each set has been used."
            for i in range(15):
                output_string += "0" + ","
        elif response4 == "n":
            print "Closing the program."
            for i in contents_backup:
                output_string += str(i) + ","
elif response2 == "n":
    print "Still in progress - will continue prompting"

#Clearing records file, writing records, and closing the file
target.seek(0)
target.truncate()
target.write(output_string)
target.close()
