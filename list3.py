# def greet(x,y):
#     z=[]
#     for w in x:
#         z=w.append(y)
#     return "Hi your ful name is : %s \n your firstname: %s \n lastname: %s" %(z.title(),x,y)
 
# f_name=[]
# l_name=[]
# f_name=list(input("enter your firstname : ")) 
# l_name=list(input("entere your lastname: "))
 
# print(greet(f_name,l_name))


temp=[9.9,8.4,8.6,3.2,3.8]

for t in temp:
    print("the round of for this list no %s is : "%t,round(t))

y=["mohammed"]
z=["azim"]
for w in z:
    v=w.title()
    y.append(v)

print(y)
