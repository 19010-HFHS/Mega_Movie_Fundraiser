#Functions

def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response
    else:
      print("Sorry - this cannot be blank")

#Main Routine

name = not_blank("Name: ")