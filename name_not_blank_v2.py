#Functions

def not_blank(question, error_message):
  valid = False

  while not valid
    response = input(question):

    if response != "":
      return response
    else:
      print(error_message)

#Main Routine

name = not_blank("Name: ", "Sorry, this cannot be blank - please enter your name")