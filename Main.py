from os import system as sys
from colorama import Fore as f, Back as b, Style as s
from random import randint as rn
from time import sleep
sys('cls'or'clear')
## --- number setting --- ##
print(b.BLACK+f.CYAN+"\tNumber Generator Mola!\n\t\tv1.0")
print(f.WHITE+"\n\nplease enter a range like (912)")
range_ = input(f.YELLOW+">> "+f.WHITE)
print("please enter number of PhoneNumber")
loops = int(input(f.YELLOW+">> "+f.WHITE))
sys('cls'or'clear')
## --- output step 1 --- ##
output = open("output.txt",'w+')
## --- generation and output --- ##
for i in range(loops):
    Number = rn(1111111, 9999999)
    output.writelines("+98"+range_+str(Number)+"\n")
    print(f.MAGENTA+"+98 "+range_+f.YELLOW+str(Number))
