year=input('Enter year:')
l=[]
try:
# open measles.txt files and read in betweeen the lines("r")
    with open('measles.txt', 'r') as f:
    # loop through the file line by line part_A.playGuide
        for lines in f:
            line = lines.split()
            if line:
                if year in ["ALL", 'all', '']:
                    l.append(lines)
                elif line[4].startswith(year):
                    l.append(lines)

except IOError:
    print('Could not read file')
if l:
    file=input("Enter name of file in which data will be written: ")
    with open(file,'w') as f:
        for lines in l:
            f.write(lines)