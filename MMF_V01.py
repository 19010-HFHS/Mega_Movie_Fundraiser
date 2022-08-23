#  import statements


#  functions
count = 0
MAX_TICKETS = 5

    

#  main routine goes here
#  --------Main Routine--------
while name != "xxx" and count < MAX_TICKETS:
#  Set up dictionaries / lists needed to hold data

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
      
    if count < 4: 
      print("You have {} seats "
      "left".format(MAX_TICKETS - count))
  # warns the user only one seat is left
    else:
      print("*** THERE IS ONE SEAT LEFT!! ***")
count += 1

if count == MAX_TICKETS:
  print("You have sold all the available tickets!")
else: print("You have sold {} tickets. \n"
 "there are {} seats still available".format(count, MAX_TICKETS - count))

  


  #  Calculate ticket price

  #  Loop to ask for snacks