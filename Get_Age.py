#  function goes here



def int_check(question, low_num, high_num):

  #  error message
  Error = "Please enter a whole number between {} and {}".format(low_num, high_num)
  
  valid = False
  while not valid:
   #  ask user for number and check it is valid
    try:
      response = int(input(question))
      return response
    #  if an integer is not entered, display an error
    except ValueError:
      print(Error)
#  main routine goes here
age = int_check("Age: ", 12, 130)
if age < 12:
  print("Please enter a whole number between 12 and 130")

elif age > 130:
  print("Please enter a whole number between 12 and 130")