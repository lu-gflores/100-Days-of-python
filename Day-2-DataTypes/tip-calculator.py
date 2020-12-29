
print('Welcome to the tip calculator!')
total_bill = input('What was the total bill? $')
percent_tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
num_people = input('How many people to split the bill? ')

result = (float(total_bill) / int(num_people)) * ((int(percent_tip) / 100) + 1)

final_amount = "{:.2f}".format(result, 2)
print(f"Each person should pay ${final_amount}")