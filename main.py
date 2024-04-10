from func.gen_password import gen_password
from func.verify_answer import verify_answer
import pyperclip


## Path to the key file
path = "key/key_generate.pub"

## Create list Uppercase / Lowercase / Number / Specials Characters
lowercase = [chr(i) for i in range(97, 123)]
uppercase = [chr(i) for i in range(65, 91)]
number = [chr(i) for i in range(48, 58)]
char_spe = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)]

## Config file
configuration = [uppercase, lowercase, number, char_spe]

## Set questions
questions = ["Uppercase", "Lowercase", "Number", "Special characters"]

## Set list 
tab = {}
excluding_char= []

# Start Program
print("How much characters do you want ?")
length = input("Enter a number : ")

## Try to convert 'length' value to int
try:
    tab[4] = int(length)
except Exception as inst:
    print(f"Invalid entry. \n Exit program - code 1 : {inst.args}")
    exit(1)

## Ask option
for i in range(len(questions)):
    print("Do you want " + questions[i] + "?")
    val = input("(y/n) : ")
    val = verify_answer(val, i, excluding_char)
    tab[i] = val
print(tab)
print(excluding_char)

## Generate key
val = gen_password(tab, configuration, excluding_char)

## Print result 
print("Result :", val)
print('---------------------------------------------------')
print("The key is copied to the clipboard")

## Copy key to the clipboard
pyperclip.copy(val)

## Write key in the file key_generate.pub
with open(path, 'w') as key:
    key.write("-----BEGIN KEY-----\n")
    key.write(val)
    key.write("\n-----END KEY-----")