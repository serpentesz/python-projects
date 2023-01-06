import random
import string

letters = string.ascii_letters
ledisi = string.ascii_letters + string.digits + string.punctuation
ledi = string.ascii_letters + string.digits
lesi = string.ascii_letters + string.punctuation

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


def Generate(Letters, Digits, Signs):
  if Digits == True and Signs == False:
    passes = random.choices(ledi, k=16)
    password = shuffle(''.join(passes))
    print(password)
  elif Digits == True and Signs == True:
    passes = random.choices(ledisi, k=16)
    password = shuffle(''.join(passes))
    print(password)
  elif Digits == False and Signs == True:
    passes = random.choices(lesi, k=16)
    password = shuffle(''.join(passes))
    print(password)
  elif Digits == False and Signs == False:
    passes = random.choices(letters, k=16)
    password = shuffle(''.join(passes))
    print(password)
  
Generate(16, False, False)

