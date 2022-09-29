import re

#  Function goes here
def string_check(choice, options):

  for var_list in options:

    #  if the snack is one of the lists, return the full name
    if choice in var_list:

      #  Get full name o snack and put it in title case so that it looks nice when outputed
      chosen = var_list[0].title()
      is_valid = "yes"
      break

    #  if the chosen option is not valid, set is_valid to no
    else:
      is_valid = "no"

#  if the snack is not OK - ask question again.
  if is_valid == "yes":
    return chosen
  else:
    return "invalid choice"
    

def get_snack():
  #  Regular expression to find if item starts with a number
  number_regex = "^[1-9]"

  #  valid snacks holds list of all snacks. Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>
  valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "e"]
  ]

  #  holds snack order for a single user
  snack_order = []

  #  holds variable for desired snack for the exit code
  desired_snack = ""

  #  If they say yes, ask what snacks they want

  if check_snack == "Yes":

    while desired_snack != "xxx":

      snack_row = []
    
      #  ask user for desired snack and put it in lowercase
      desired_snack = input("Snack: ").lower()

      if desired_snack == "xxx":
        return snack_order

  
      #  if item has a number, seperate it into two (number / item)
      if re.match(number_regex, desired_snack):
        amount = int(desired_snack[0])
        desired_snack = desired_snack[1:]


      else:
        #  if item does not have a number in front, set number to 1
        amount = 1
        desired_snack = desired_snack

      #  remove white space around snack
      desired_snack = desired_snack.strip()
    
      #  check if snack is valid
      snack_choice = string_check(desired_snack, valid_snacks)

  #  check snack amount is valid (less than 5)
    if amount >= 5:
      print("Sorry - we have a four snack maximum")
      snack_choice = "invalid choice"
    elif amount == float():
      print("Please enter a valid  number")
      snack_choice = "invalid choice"
  #  add snack AND amount to list...
  
      snack_row.append(amount)
      snack_row.append(snack_choice)

  #  check that snack is not the exit code before adding
    if snack_choice != "xxx" and snack_choice != "invalid choice":
      snack_order.append(snack_row)

#  Main Routine goes here
#  valid options for yes / no questions
yes_no = [
  ["yes", "y"],
  ["no", "n"]
]  

#  ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid  choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack =  string_check(want_snack, yes_no)

#  If they say yes, ask what snacks they want (and add to our snack order)
if check_snack == "Yes":
  get_order = get_snack()

else:
  get_order = []

#  Show snack orders
print()
if len(get_order) == 0:
  print("Snacks Ordered: None")

else:
  print("Snacks Ordered: ")

print(get_order)