#acsseing file using 'with' and 'as' keyword
with open("fruits.txt") as my_file:
    content=my_file.read()

print(content)    