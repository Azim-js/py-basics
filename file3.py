#to write mode to create and write in a file

with open("vwegetables.txt","w+") as my_file:
    my_file.write("tomato\nheloo\norange\n")
    my_file.write("mango")
    my_file.seek(0)
    content=my_file.read()
print(content)    
    
# x=input("enter the list elements using space ")
# print(len(x.split()))
# print(type(x))