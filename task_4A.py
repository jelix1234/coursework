import random
# open text file a,txt from the file directory which incude random interger list
file1 = open("A.txt", "w")
for i in range (500):
  number = str(random.randint(0,500))
  file1.write(number)
  file1.write("\n")
file1.close
