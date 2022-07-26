#  start of loop

#  initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < 4:
  print("You have {} seats "
  "left".format(MAX_TICKETS - count))
  
  if count == 4:
    print("*** THERE IS ONE SEAT LEFT!! ***")
  
  #  Get details...
  name = input("Name: ")
  count += 1
  print()

if count == MAX_TICKETS:
  print("You have sold all the available tickets!")
