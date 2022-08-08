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

#  --------Main Routine--------

#  Set up dictionaries / lists needed to hold data

def not_blank(question):

  #  Get name (can't be blank)
  name = not_blank("Name: ")

  #  end the loop if the exit code is entered
  if name == "xxx":
    break

  count += 1
  print()


  #  Get age (between 12 and 130)
  age = int_check("Age: ", 12, 130)


#  End of tickets loop
if count == MAX_TICKETS:
  print("You have sold all the available tickets!")
else: print("You have sold {} tickets. \n"
 "there are {} seats still available".format(count, MAX_TICKETS - count))

  #  Get age (between 12 and 130)
  


  #  Calculate ticket price

  #  Loop to ask for snacks