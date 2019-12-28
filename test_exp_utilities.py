'''
Author @ Richard Whittle
Created @ 2019 12 28
Note: base tests written for utilities expenses
'''

from calculate_expenses import monthly_electricity_bill
from calculate_expenses import monthly_gas_bill
from calculate_expenses import monthly_telephony_bill

# Monthly Electric Bill Calculations
test_Elec_nil = 0
test_Elec_low = 20
test_Elec_high = 50
test_Elec_alpha = "Electric"
test_Elec_neg = -20

assert monthly_electricity_bill(test_Elec_nil) == 0
assert monthly_electricity_bill(test_Elec_low) == 4.49
assert monthly_electricity_bill(test_Elec_high) == 11.24
assert monthly_electricity_bill(test_Elec_alpha) == 0
assert monthly_electricity_bill(test_Elec_neg) == 0

# Montly Gas Bill Calculations
test_Gas_nil = 0
test_Gas_low = 15
test_Gas_high = 50
test_Gas_alpha = "gas"
test_Gas_neg = -20

assert monthly_gas_bill(test_Gas_nil) == 0
assert monthly_gas_bill(test_Gas_low) == 3.37
assert monthly_gas_bill(test_Gas_high) == 11.24
assert monthly_gas_bill(test_Gas_alpha) == 0
assert monthly_gas_bill(test_Gas_neg) == 0

# Monthly Telephony Bill Calculations
test_Telephony_nil = 0
test_Telephony_low = 20
test_Telephony_high = 100
test_Telephony_alpha = "Telephone"
test_Telephony_neg = -30

assert monthly_telephony_bill(test_Telephony_nil) == 0
assert monthly_telephony_bill(test_Telephony_low) == 4.49
assert monthly_telephony_bill(test_Telephony_high) == 22.47
assert monthly_telephony_bill(test_Telephony_alpha) == 0
assert monthly_telephony_bill(test_Telephony_neg) == 0
