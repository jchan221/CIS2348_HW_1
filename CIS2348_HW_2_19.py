# Joshua Chan
# 1588459
lemon = float(input('Enter amount of lemon juice (in cups):''\n'))
water = float(input('Enter amount of water (in cups):''\n'))
agave = float(input('Enter amount of agave nectar (in cups):''\n'))
servings = float(input('How many servings does this make?''\n''\n'))
# The prompts above will find the measurements for the lemonade
print('Lemonade ingredients - yields',('{:.2f}'.format(servings)),'servings')
print(('{:.2f}'.format(lemon)),'cup(s) lemon juice')
print(('{:.2f}'.format(water)),'cup(s) water')
print(('{:.2f}'.format(agave)),'cup(s) agave nectar''\n')
# The output above will confirm the recipe
user_serve = float(input('How many servings would you like to make?''\n''\n'))
new_measure = user_serve/servings
print('Lemonade ingredients - yields',('{:.2f}'.format(servings * new_measure)),'servings')
print(('{:.2f}'.format(lemon * new_measure)),'cup(s) lemon juice')
print(('{:.2f}'.format(water * new_measure)),'cup(s) water')
print(('{:.2f}'.format(agave * new_measure)),'cup(s) agave nectar''\n')
# The recipe will be converted to the serving size required by the user
print('Lemonade ingredients - yields',('{:.2f}'.format(servings * new_measure)),'servings')
print(('{:.2f}'.format(lemon * new_measure / 16)),'gallon(s) lemon juice')
print(('{:.2f}'.format(water * new_measure / 16)),'gallon(s) water')
print(('{:.2f}'.format(agave * new_measure / 16)),'gallon(s) agave nectar')
# Recipe will be converted from cups to gallons




