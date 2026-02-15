import random 
import string

length = int(input(" Parol uzunligini kiriting: " ))

characters = string.ascii_letters + string.digits + string.punctuation 

password = ''.join(random.choice(characters) for i in range(length))

print("Yaratilgan parol:",password)
print("Updated by Davlatnazir")
