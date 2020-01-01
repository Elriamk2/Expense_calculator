'''
test National Insurance Function
Created 01/01/2020
Author @ Richard Whittle
'''

from current_income_expenses import national_insurance

# create national insurance test statements
ni_alpha = "National Insurance"
ni_blank = ""
ni_low = 5000
ni_medium = 15000
ni_high = 60000

# Create national insurance asserts
assert national_insurance(ni_alpha) == 0
assert national_insurance(ni_blank) == 0
assert national_insurance(ni_low) == 0
assert national_insurance(ni_medium) == 15
assert national_insurance (ni_high) == 83