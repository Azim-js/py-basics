def deco(func):
  def inner(name):
    if name=="Sunny":
      print("Hello Sunny Bad Morning")
    else:
      func(name)
  return inner

def wish(name):
  print("Hello",name,"Good Morning")
  
decorFunction=decor(wish)

wish("Azim")#decorator will not be executed
wish("Sunny")#decorator will not be executed

decorfunction("Azim")#decorator will be executed
decorfunction("Sunny")#decorator will be executed

