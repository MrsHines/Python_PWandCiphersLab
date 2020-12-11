# Passwords and Cryptography

## How safe is your password
Given the constraints that occur on password creation, how long would it take a computer to figure out your password? 
Let’s start with a basic example, suppose you have a 4-character password composed of only lower case letters.  How many times would a computer need to try your password to get it correct?  How long would it take?  (Not as long as you think…)

Write the following functions to see.

### Function #1 – passCheck4(pw)
Write a function that will attempt to crack a given 4-character password.  The actual password should be passed in through a parameter.  It should be compared to the passwords produced by the function.  The function should return the number of guesses it took to crack the password.  

### Function #2 – passCheck5(pw)
Write another function for checking passwords but Increase the number of characters in the password to 5.  Return the number of guesses it took to crack the password.  Write a comment in your function about how the addition of an additional character affects the number of guesses.

### Function #3 – passCheckUpper(pw)
Write another function for checking passwords with 4 characters that can contain upper and lowercase letters.    Return the number of guesses it took to crack the password.  Does this change your algorithm?    Write a comment in your function about how the number of guesses varies when you add additional options for characters.  What happens if you also numbers?

## Substitution Cipher

Many people are familiar with Caesar cipher (which shifts the alphabet by a given value – a key).  However, the Caesar cipher is not very secure.  It can often be cracked without the need for a computer.  A Substitution cipher is much more secure than the Caesar cipher (although still not very secure).  To create a substitution cipher, you mix up or randomly order the letters in the alphabet.  The new mixed-up version becomes the key and the index in the key corresponds to the index from the alphabet.  

### Function #4 subCipher(key, message, encrypt)
Write a function that, given a key (mixed up alphabet) and a message, will either encrypt or decrypt your message according to the boolean value encrypt.  When encrypt is true, the function will take the key and the message and will encode it.  When encrypt is false, the function will take the key and the encrypted message and will decrypt the message back to its original value.

For this one, make sure you include a " " as an option in your alphabet list.  We will do the entire message in lowercase letters for simplicity, but you could include uppercase ones too.
  
