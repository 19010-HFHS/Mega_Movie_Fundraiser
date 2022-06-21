#  import statements


#  functions

def not_blank(question, error_message)
  valid = False

  while not valid
    response = input(question)

    if response != "":
      return response
    else:
      print(error_message)

#  --------Main Routine--------

name = not_blank("Name: ", "Sorry, this cannot be blank - please enter your name")

#  Set up dictionaries / lists needed to hold data

#  Ask user if they have used the program before and show instructions if they haven't

#  Loop to get ticket details

  #  Get name (can't be blank)
  
  #  Get age (between 12 and 130)
  
  #  Calculate ticket price
  
  #  Loop to ask for snacks

  #  Calculate snack price

  #  ask for payment method (and apply surcharge if necessary)


#  Calculate Total sales and profit

#  Output data to text file