#  function goes here



def int_check(question, low_num, high_num):

  #  error message
  Error = "Please enter a whole number between {} and {}".format(low_num, high_num)
  
  valid = False
  while not valid:
   #  ask user for number and check it is valid
    try:
      response = int(input(question))
      
      if low_num < response < high_num:
        return response
      else:
        print(Error)
        
    #  if an integer is not entered, display an error
    except ValueError:
      print(Error)
#  main routine goes here
age = int_check("Age: ", 12, 130)