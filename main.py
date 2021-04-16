# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
name_indexs = len(names)
name_number = random.randint(0, name_indexs)
print(names[name_number])