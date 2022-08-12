#  import statements


#  functions

#  'name not blank' function
#  check name not blank
def not_blank(question):
  valid = False

  #  print error message if name is blank
  while not valid:
    response = input(question)

    if response != "":
      return response
    else:
      print("Sorry - this cannot be blank, please enter your name")

#checks for an integer between 12 and 130
def int_check(question):

  #  error message
  Error = "Please enter a whole number that is more than zero".format(question)
  
  valid = False
  while not valid:
   #  ask user for number and check it is valid
    try:
      response = int(input(question))
      
      if response <= 0
        print(Error)
      else:
        return response
        
    #  if an integer is not entered, display an error
    except ValueError:
      print(Error)
#  main routine goes here
#  --------Main Routine--------

#  Set up dictionaries / lists needed to hold data

def not_blank(question):

  #  Get name (can't be blank)
  name = not_blank("Name: ")

  #  end the loop if the exit code is entered
  if name == "xxx":
    break

  count += 1


  #  Get age (between 12 and 130)
  age = int_check("Age: ", 12, 130)

  #  ckeck that age is valid...
  if age < 12:
    print("Sorry, you are too young for this movie")
    continue
  elif age > 130:
    print("That is very old, it seems there's been a mistake")
    continue


#  End of tickets loop
if count == MAX_TICKETS:
  print("You have sold all the available tickets!")
else: print("You have sold {} tickets. \n"
 "there are {} seats still available".format(count, MAX_TICKETS - count))

  


  #  Calculate ticket price

  #  Loop to ask for snacks