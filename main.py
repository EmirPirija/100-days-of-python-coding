print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
perc_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
split_bill = int(input('How many people to split the bill? '))

# Calculate the tip amount
tip_amount = total_bill * (perc_tip / 100)

total_per_person = (total_bill + tip_amount) / split_bill

print(f'Each person should pay: ${total_per_person}')
