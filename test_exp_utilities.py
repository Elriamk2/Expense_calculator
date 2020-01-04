'''
Author @ Richard Whittle
Created @ 2019 12 28
Note: base tests written for utilities expenses
'''

from calculate_expenses import monthly_electricity_bill
from calculate_expenses import monthly_gas_bill
from calculate_expenses import monthly_telephony_bill

# Monthly Electric Bill Calculations
test_Elec_nil = monthly_electricity_bill(0)
test_Elec_low = monthly_electricity_bill(20)
test_Elec_high = monthly_electricity_bill(50)
test_Elec_alpha = monthly_electricity_bill("Electric")
test_Elec_neg = monthly_electricity_bill(-20)

assert test_Elec_nil[1] == 0
assert test_Elec_low[1] == 4.49
assert test_Elec_high[1] == 11.24
assert test_Elec_alpha[1] == 0
assert test_Elec_neg[1] == 0

# Montly Gas Bill Calculations
test_Gas_nil = monthly_gas_bill(0)
test_Gas_low = monthly_gas_bill(15)
test_Gas_high = monthly_gas_bill(50)
test_Gas_alpha = monthly_gas_bill("gas")
test_Gas_neg = monthly_gas_bill(-20)

assert test_Gas_nil[1] == 0
assert test_Gas_low[1] == 3.37
assert test_Gas_high[1] == 11.24
assert test_Gas_alpha[1] == 0
assert test_Gas_neg[1] == 0

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
