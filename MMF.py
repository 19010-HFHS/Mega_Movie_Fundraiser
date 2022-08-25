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

#checks for an integer that is more than 0
def int_check(question):

  #  error message
  error = "Please enter a whole number that is more than zero"
  
  valid = False
  while not valid:
   #  ask user for number and check it is valid
    try:
      response = int(input(question))
      
      if response <= 0:
        print(error)
      else:
        return response
        
    #  if an integer is not entered, display an error
    except ValueError:
      print(error)
# ********** Main Routine ************

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details
# start of loop

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

while name != "xxx" and ticket_count < MAX_TICKETS:
#  Set up dictionaries / lists needed to hold data
    if ticket_count < MAX_TICKETS - 1: 
      print("You have {} seats "
      "left".format(MAX_TICKETS - ticket_count))
  # warns the user only one seat is left
    else:
      print("*** THERE IS ONE SEAT LEFT!! ***")
      
  #  Get name (can't be blank)
    name = not_blank("Name: ")
  #  end the loop if the exit code is entered
    if name == "xxx":
      break
#  Get age (between 12 and 130)
    age = int_check("Age: ")
#  ckeck that age is valid...
    if age < 12:
      print("Sorry, you are too young for this movie")
      continue
    elif age > 130:
      print("That is very old, it seems there's been a mistake")
      continue


    if age < 16:
      ticket_price = 7.5
    elif age <= 65:
      ticket_price = 6.5
    else:
      ticket_price = 10.5

  
    ticket_count += 1
    ticket_sales += ticket_price
#  end of tickets loop
#  calculate ticket profit...
ticcket_profit = ticket_sales - (5 * ticket_count)
print("Ticket Profit: ${:.2f}".format(ticket_profit))

#  tell the user if they have unsold tickets
if ticket_count == MAX_TICKETS:
  print("You have sold all the available tickets!")
else: 
  print("You have sold {} tickets. \n"
 "there are {} seats still available".format(ticket_count, MAX_TICKETS - ticket_count))