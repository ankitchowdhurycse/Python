#Checks if entered string is palindromic

text = input("Enter the string: ")

if (text == text[::-1]):
  print("%s is a palindromic string" %(text))
else:
  print("%s is not a palindrome" %(text))
