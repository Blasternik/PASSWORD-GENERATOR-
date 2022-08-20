import random #Modules needed 
from secrets import choice #Modules needed

print ('''<FREE PASSWORD GENERATOR POWERED BY Blasternik!> :)''') #Welcome adversite

caratteri= '''abcdefghilmnopqrstuvzwxy1234567890ABCDEFGHILMNOPQRSTUVZXYW?!-\&%''' #Pool of char

lunghezza= int  (input ('''INSERIRE LUNGHEZZA PASSWORD (DECIMALE)''')) #legth of password chosen by use

password = "" #Starting password

for x in range (lunghezza):
     password+= random.choice (caratteri) #For all element in range (lunghezza), random modules add char to password variables from caratteri pool

print ('''ecco la tua nuova password:''', password) #New password variables after for cycle