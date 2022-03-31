import random

file1 = open("A.txt", "w")
for i in range (100):
  number = str(random.randint(0,100))
  file1.write(number)
  file1.write("\n")
file1.close