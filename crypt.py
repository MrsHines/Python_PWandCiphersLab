import random

def passCheck4(pw):
  guess = ''
  alpha_choices = 'abcdefghijklmnopqrstuvwxyz '
  count = 0

  for i in range(len(alpha_choices)):
    for j in range(len(alpha_choices)):
      for k in range(len(alpha_choices)):
        for l in range(len(alpha_choices)):
          guess = alpha_choices[i] + alpha_choices[j] + alpha_choices[k] + alpha_choices[l]
          count = count + 1
          if guess == pw:
            return guess, count

def passCheck5(pw):
  guess = ''
  alpha_choices = 'abcdefghijklmnopqrstuvwxyz '
  count = 0

  for i in range(len(alpha_choices)):
    for j in range(len(alpha_choices)):
      for k in range(len(alpha_choices)):
        for l in range(len(alpha_choices)):
          for m in range(len(alpha_choices)):
            guess = alpha_choices[i] + alpha_choices[j] + alpha_choices[k] + alpha_choices[l] + alpha_choices[m]
            count = count + 1
            if guess == pw:
              return guess, count

def passCheckUpper(pw):
  guess = ''
  alpha_choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  count = 0

  for i in range(len(alpha_choices)):
    for j in range(len(alpha_choices)):
      for k in range(len(alpha_choices)):
        for l in range(len(alpha_choices)):
            guess = alpha_choices[i] + alpha_choices[j] + alpha_choices[k] + alpha_choices[l]
            count = count + 1
            print(count)
            if guess == pw:
              return guess, count

def subCipher(key, message, encrypt):
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  new_message = ""
  for let in message:
    if encrypt:
      new_message = new_message + key[alphabet.find(let)]
    else:
      new_message = new_message + alphabet[key.find(let)]
  return new_message

def main():
  
  passw, times = passCheck4("abcd")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")

  passw, times = passCheck4("jdti")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")

  passw, times = passCheck5("aabbc")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")

  """
  passw, times = passCheckUpper("jDtI")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")
  """

  print(subCipher("_aeioubcdfghjklmnpqrstvwxyz", "hello world", True))
 
  print(subCipher("_aeioubcdfghjklmnpqrstvwxyz", "cohhlzvlphi" , False))

  print(subCipher("_aeiouzyxwvtsrqpnmlkjhgfdbc", "hello world", True))
 
  #print(subCipher("_aeiouzyxvtsrqpnmlkjhgfdbc", "" , False))





if __name__ == '__main__':
  main()
