def Process(f):
    years=input('Enter years:')
    #  input the year details you want to check 
    # income represented as Inc 
    Inc = int(input('Enter Income Level from set{1,2,3,4} :'))
    Inc_level = "";
    if Inc == 1:
        Inc_level = "WB_LI";
    if Inc == 2:
        Inc_level = "WB_LMI";
    if Inc == 3:
        Inc_level = "WB_UMI";
    if Inc == 4:
        Inc_level = "WB_HI";
    if Inc < 1 or Inc > 4:
        Inc_level = "WB_LMI";
    l= []
    high = 0;
    low = 100;
    total = 0;
    for lines in f:
        line = lines.split()
        if line:
            print(str(line[1]))
            if line[4].startswith(years) and line[1] == Inc_level:
                l.append(lines)
                total = total + int(line[2])
                if high < int(line[2]):
                    high = int(line[2])
                if low > int(line[2]):
                    low = int(line[2])
    lower_con = []
    high_con = []
    for lines in l:
        line = lines.split()
        if line:
            if int(line[2]) == high:
                high_con.append(line[0]);
            if int(line[2]) == low:
                lower_con.append(line[0]);
    if l:
        print("count of report = "+str(len(l)))
        print("Avarage percentage = ",float(total)/float(len(l)))
        print("lowest percentage countries = "+str(lower_con))
        print("highest percentage countries = "+str(high_con))
    else:
        print('No data to display report')

def O_file():
    n = True
    file_name = "";
    while n:
        file_name = input('Enter Input File Name : ')
        try:
            f = open(str(file_name), 'r')
            if f:
                return f;
        except IOError:
            n = True


def main():
    f = O_file();
    Process(f)

main()