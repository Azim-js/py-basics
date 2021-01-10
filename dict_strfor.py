print("to access the formated string in a dictionary by simple for loop {}{} .format(variable[0],variable[1])")
student_grades={"azim":"A","shabnam":"D","rian":"A","aamir":"A"}

for a in student_grades.items():
    print("{} has got the grade : {}".format(a[0].title(),a[1]))

print("to access the formated string in a dictionary by key,values {}{} .format(keys,values)")
names_meaning={"azim":"cant estimate","rian":"prince","shabnam":"pores","aamir":"prouspers"}

for keys,values in names_meaning.items():
    print("{}'s meaning in english dictionary is : {}".format(keys,values))
