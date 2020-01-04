'''
test National Insurance Function
Created 01/01/2020
Author @ Richard Whittle
'''

from current_income_expenses import national_insurance

# create national insurance test statements
ni_alpha = national_insurance("National Insurance")
ni_blank = national_insurance("")
ni_low = national_insurance(5000)
ni_medium = national_insurance(15000)
ni_high = national_insurance(60000)

# Create national insurance asserts
assert ni_alpha[1] == 0
assert ni_blank[1] == 0
assert ni_low[1] == 0
assert ni_medium[1] == 15
assert ni_high[1] == 83