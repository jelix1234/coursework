# the program written below is to encode,decrypt and quit when some particular keys are inputed
def enc():
    text, s = input("Enter the string to be encoded: "), int(input("Enter the shift value(1-25): "))

    result = ""
    # 
    for i in range(len(text)):
        char = text[i]
     

        if char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        
        else:
            result += char

    print("Encrypted text: ", result)


 ''' code to decruypt file'''
def dec():
    message, s = input("Enter the string to be decoded: "), input("Enter the word from plaintext: ")

    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        if s in translated:
            break
    print('The encryption key is: %s\n Plaintext: %s' % (key, translated))

 # regarding the input file,it was referenced from the example output from the assigment brie
while True:
    ch = input("\nEnter \n'e' to encrypt\n'd' to decrypt\n'q' to quit:\n")
    if ch == 'e':
        enc()
    elif ch == 'd':
        dec()
        input("bad command,try again")
    elif ch == 'q':
        input ("thanks for playing")
        break
    else:
        print("Wrong input! Try again: ")