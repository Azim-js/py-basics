temps=[220,330,221,440]

new_temp=[temp/10 for temp in temps]

print(new_temp)

temps1=[221,330,-999,780]

new_temps=[x/10 for x in temps1 if x !=-999]

print(new_temps)