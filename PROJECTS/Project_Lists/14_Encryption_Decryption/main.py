# encryption program
"""
import string
import random
chars = string.punctuation + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)
# print(f'chars:{chars}')
# print(f'key:{key}')

plain_text = input('enter a message to encrypt: ')
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f'orginal message:{plain_text}')
print(f'encrypted message:{cipher_text}')


cipher_text = input('enter a message to de-encrypt: ')
plain_text=""

for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f'orginal message:{cipher_text}')
print(f'encrypted message:{plain_text}')"""
