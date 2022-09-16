

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





#  valid snacks holds list of all snacks. Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>

valid_snacks = [
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "d"]
]

#  valid options for yes / no questions
yes_no = [
  ["yes", "y"],
  ["no", "n"]
]

#  holds the snack order for a single user
snack_order = []

#  holds the variable for the desired snack for exit code
desired_snack = ""

check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no)

#If they say yes, ask what snacks they want
if check_snack == "Yes":

  while desired_snack != "xxx":
    #  ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()

    if desired_snack == "xxx":
      break

    #  check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)

    # add snack to list...

    #check that snack is not the exit code before adding
  
    if snack_choice != "xxx" and snack_choice != "invalid choice":
      snack_order.append(snack_choice)


#  Show snack orders
print()
if len(snack_order) == 0:
  print("Snacks Ordered: None")

else:
  print("Snacks Ordered: ")

  for item in snack_order:
    print(item)


while desired_snack != "xxx" and check_snack != "No":
#  loop six times to make testing quicker
  for item in range(0, 6):
    #  ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()
  
    #  check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)
