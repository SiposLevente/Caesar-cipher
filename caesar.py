import os
os.system('clear')

offset = 4

def encrypt(STRING, offset):
    a = list(STRING)
    b = []
    for i in a:
        b.append(ord(i))
    for i in range(len(b)):
        b[i-1] = b[i-1]+offset
    c = ""

    for i in b:
        c = c + chr(i)
    return c

def decrypt(STRING, offset):
    a = list(STRING)
    b = []
    for i in a:
        b.append(ord(i))
    for i in range(len(b)):
        b[i-1] = b[i-1]-offset
    c = ""
    for i in b:
        c = c + chr(i)
    return c

def encryptFile(FILE, offset):
    data = open(str(FILE), "r")
    x = data.readlines()
    a = ""

    for i in x:
        a = a + str(i)
    a = encrypt(a,offset)
    data.close()

    data = open("Encrypted"+str(FILE),"w")
    data.write(str(a))
    data.close()

def decryptFile(FILE, offset):
    data = open(str(FILE), "r")
    x = data.readlines()
    a = ""
    for i in x:
        a = a + str(i)
    a = decrypt(a,offset)
    data.close()

    data = open("Decrypted"+str(FILE),"w")
    data.write(str(a))
    data.close()

offset = 4
lastString = ""
stringEdit = ""
fileEdit=":"

while True:
    print("Caesar Cipher\nPrevious"+ stringEdit+" output: " + lastString + ". Previous file" + fileEdit + "\n\n")
    print("1 - Encript string\n2 - Decript string\n\n3 - Encript file\n4 - Decript file\n\n5 - Change offset (current: %a)\n6 - Exit" %offset)
    print("\n\nIf choosing a file to decrypt/encrypt make sure that the file is in the same directory as the program!")
    a = input("Input a number: ")

    if(a == "1"):
        x = encrypt(input("Encrypt string output: "),offset)
        lastString = x
        stringEdit = " encryption's"
    elif(a == "2"):
        x = decrypt(input("Decrypt string output: "),offset)
        lastString = x
        stringEdit = " decryption's"
    elif(a == "3"):
        x = input("Encrypt file: ")
        encryptFile(x,offset)
        fileEdit = " encrypted as: Encrypted"+x
    elif(a == "4"):
        x = input("Decrypt file: ")
        decryptFile(x,offset)
        fileEdit = " decrypted as: Decrypted"+x 
    elif(a == "5"):
        offset = int(input("Input new offset: "))
    elif(a == "6"):
        break
    else:
        print("This input is invalid!")
    os.system("clear")
