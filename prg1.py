def sentence_maker(phrase):
    interogatives=("What","Why","How")
    capital=phrase.capitalize()
    if capital.startswith(interogatives):
        return "{}?".format(capital)
    else:
        return"{}.".format(capital)

result=[] #for appending the totoal user input

while True:
    user_input=input("say something : ")
    if user_input=="\end":
        break
    else:
        result.append(sentence_maker(user_input))
print(" \n".join(result))        

