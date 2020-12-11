import random

def passCheck4(pw):
  guess = ''
  alpha_choices = 'abcdefghijklmnopqrstuvwxyz '
  count = 0
  
  #Finish the code for this function here

def passCheck5(pw):
  guess = ''
  alpha_choices = 'abcdefghijklmnopqrstuvwxyz '
  count = 0

  #Finish the code for this function here.
  #I left the return statement so that you can see how we return two things at once.
              return guess, count

def passCheckUpper(pw):
  guess = ''
  alpha_choices = 'abcdefghijklmnopqrstuvwxyz'  #What do you need to do to your list of alphabet choices?
  count = 0
  
  #Finish the code for the function here
  #I left the return statement so you can see how we return two things at once.
              return guess, count

def subCipher(key, message, encrypt):
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  new_message = ""
  #Finish the function here

def main():
  
  """
  Some of these functions take longer to run.  You may consider adding print statements into the functions so that you can watch them run.
  I would only uncomment and run one of the password checkers at a time.  
  
  passw, times = passCheck4("abcd")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")

  passw, times = passCheck4("jdti")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")

  passw, times = passCheck5("aabbc")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")

  
  passw, times = passCheckUpper("jDtI")
  print("Your password is :" + passw)
  print("It took " + str(times) + " tries to crack it")
  

  print(subCipher("_aeioubcdfghjklmnpqrstvwxyz", "hello world", True))
 
  print(subCipher("_aeioubcdfghjklmnpqrstvwxyz", "cohhlzvlphi" , False))

  print(subCipher("_aeiouzyxwvtsrqpnmlkjhgfdbc", "hello world", True))
  
 """





if __name__ == '__main__':
  main()
