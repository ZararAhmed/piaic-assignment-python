
#############################
# stringtypes,case-sensitiveness, in-memory, out-of-memory

name1 = "zarar"
name2 = "ahmed"

# print("name1 == name2:", name1 == name2)
# print(id(name1), id(name2), sep="\n")
# print(name1, name2, sep="\n")
# print(name1.isprintable())
print(dir(name1))
# print(name1.title())


# deleting variables
# del name1
# print(name1)


# length
# print(len(name1))


# strip
name3 = "   Hamza   "
# print(name3.strip())


# find
a = "bnmj  kjhk Pakistan nlihi Pakistan kh"
# print(a.find("Pakistan"))


# slicing
# print(a[10:18:1]) #start:end:step    important points in slicing
# print(a[a.find("Pakistan"):18])
# print(a.count("Pakistan"))
# print(a.split())


# Concatenation
name3 = 'hamza'
fname = 'Muhammad'
program = 'PIAIC'

# method1
# print(" Sudent name: %s \n \
# Father's name : %s 
# %(name3,fname,program))

# method2
# print("Student name: " + name3 + "\nfather's name: " + fname + "\nprogram: " + program)

# method3 String literal
# print(f"Student Name: {name3} \nFather Name: {fname} \nProgram: {program}") 

# print("Namee: {}\nfather: {}".format(name3,fname))