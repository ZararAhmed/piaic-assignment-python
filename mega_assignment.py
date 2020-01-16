rangeI = 5
for i in range(rangeI):
    for j in range(i+1):
        print("*", end="")
    print("")


my_dict = {"name":"zarar", "age":"25"}

print(my_dict.get("zarar"))
print(my_dict.__contains__("zarar"))

####################################

# missed this question

###################################
p=3
q="hello"
print(p*q)

#################################
print(q.upper())


#####################################
p = True
q = 'True'
r = 2
s = 2.0
print(type(p))
print(type(q))
print(type(r))
print(type(s))


############################################
X=15
Y=2

print(X % Y)
print(X / Y)
print(X // Y)
print(Y % X)

#######################################
x = [[4, 1, 1], [5, 9, 0]]

# missed one part
for i in x:
    for j in i:
        print(j, end=" ")
    print()

#####################################

q = [10.62, 16.14, 6.45, 17.11]
for j, z in enumerate(q):
    print('Item '  + str( j ) + ' - ', str ( z ))

####################################### - 22

D = dict()
for i in range(3):
    for j in range(4):
        D[i] = j
        print(D[i])
print(D)

###########################################################
def increment_score(bonus, score = True, points = 1):
    print(bonus)
    print(score)
    print(points)
    return str(bonus) + ", " + str(score) + ", " + str(points) +""

print(increment_score(2))

#############################################################

def avg ( x , y , z = 50 ):
    adding = x + y + z
    avg_value = adding / 3
    return avg_value
y = avg ( x = 5 , y = 9 , z = 20 )
print(y)