# Joshua Chan
# 1588459
# Birthday Calculator
current_day = int(input('What is the calendar day?'))
current_month = int(input('What is the current month?'))
current_year = int(input('What is the current year?'))
# The three prompts above will collect the current date
birth_day = int(input('What day is your birthday?'))
birth_month = int(input('What month is your birthday?'))
birth_year = int(input('What year were you born?'))
# The three prompts above will collect the user's birthday
user_age = current_year - birth_year
if current_month > birth_month:
    print('You are', user_age, 'years old.')
if current_month < birth_month:
    print('You are', user_age - 1, 'years old.')
# Above will calculate the user's age
if current_day == birth_day and current_month == birth_month:
    print('Happy Birthday!')
    print('You are', user_age, 'years old.')
# Above will check if the current date is the user's birthday










