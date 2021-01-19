def greet(x,y):
    z=" ".join([x,y])
    return "Hi your ful name is : %s \n your firstname: %s \n lastname: %s" %(z.title(),x,y)


f_name=input("enter your firstname : ")
l_name=input("entere your lastname: ")



print(greet(f_name,l_name))

