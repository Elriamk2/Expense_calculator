from current_income_expenses import *


class national_insurance:
    def __init__(self, gross_pay):
        self.gross_pay = gross_pay

    def __repr__(self):
        return f({self.gross_pay})



# value storage list?
# current_wages gross_pay, select_tax_region, car_distance, car_trips, train_ticket_return, train_trips_per_week, council_tax_assesment, housing_payments, monthly_telephony_bill
calculations_list = [0,0,0,0,0,0,0,0,0,0]

# Basis for differential wage calculation
# calculations_list[0] = (float(input("What is your current salary? :")))
# calculations_list[0] = current_wages

while True:
    try:
        gross_pay = (input("Enter the wage you wish to calculate: "))
        calculations_list[0] = gross_pay
        break
    except:
        print("You must enter your salary as a numeric value")
        sys.exit(1)

calculations_list[1] = (input("If you live in Scotland press 1, if you live in the rest of the UK press 2: "))
if calculations_list[1] == '1':
    weekly_income = yearly_wages_scot(gross_pay)
    current_weekly_income = yearly_wages_scot(calculations_list[1])
elif calculations_list[1] == '2':
    weekly_income = yearly_wages_uk_other(gross_pay)
    current_weekly_income = yearly_wages_uk_other((float(calculations_list[0])))
else:
    weekly_income = yearly_wages_uk_other(gross_pay)
    current_weekly_income = yearly_wages_uk_other((float(calculations_list[0])))

#test_wages_scot()

# define the travel to work / secondary location costs
calculations_list[1] = (input("What is the return trip distance? If you are not using a car enter 0: "))
calculations_list[2] = (input("How many trips do you make? If you are not using a car enter 0: "))
calculate_car_travel = float(calculations_list[2]) * float(calculations_list[3])
# calculations_list[2] = car_distance
# calculations_list[3] = car_trips

weekly_car_payments = car_travel_per_trip(calculate_car_travel)

# define the train travel costs
# train_ticket_return(4.70)
calculations_list[3] = input("How many return train trips do you take per week? Enter 0 if not using a train: ")
calculations_list[4] = input("How much does your train ticket cost? Enter 0 if not using a train: ")
#calculations_list[4] =  train_trips_per_week
weekly_train_costs = train_ticket_return(float(calculations_list[3]), float(calculations_list[4]))


# Calculate housing costs, council tax band should be entered as a string
# council_tax_band("b")
calculations_list[6] = input("What council tax band is your house? Enter 0 if you are not paying council tax: ")
weekly_council_payments = council_tax_band(float(calculations_list[6]))
#calculations_list[6] = council_tax_assesment(council_tax_assesment)

# housing_payments(156)
calculations_list[7] = housing_paymentsinput("How much is your mortgage or rent? Enter 0 if you are not paying these: ")
weekly_housing_costs = housing_payments(float(calculations_list[7]))

# monthly_electricity_bill(55)
calculations_list[8] = monthly_electricity_bill(input("How much will you be paying per month for electricity? If no electic bill enter 0: "))
#calculations_list[8] = monthly_electricity_bill
weekly_electric_bill = float(monthly_electricity_bill)

# monthly_gas_bill 

# monthly_broadband = 32.99
calculations_list[9] =input("How much will you pay for telephony services monthly? If you are not paying for these enter 0: ")
monthly_telephony_bill(float(weekly_telephony))
# calculations_list[9] = weekly_telephony(weekly_telephony)
weekly_telephony = float(monthly_telephony_bill)

#additional income streams
additional_monthly_income = float(input("Enter any additional monthly income, if none, enter 0: "))

# calculate the weekly outgoings
weekly_take_home = weekly_income - weekly_car_payments - weekly_council_payments - weekly_train_costs - weekly_housing_costs - weekly_electric_bill - weekly_telephony + (additional_monthly_income / 4.35) # - weekly_gas_bill
monthly_take_home = weekly_take_home * 4.35
yearly_take_home = weekly_take_home * 52.1
current_yearly_take_home = current_weekly_income * 52.1

# print all outputs
print("=====")
print("The weekly telephony payments are", round(weekly_telephony, 2))
print("your weekly income is:", weekly_income)
print("Weekly take home pay after taxes and National Insurance is roughly:", round(weekly_take_home, 2))
print("Monthly earnings after tax and expenses is roughly", round(monthly_take_home, 2))
print("Yearly earnings after tax and expenses is roughly", round(yearly_take_home, 2))
print("The difference in current earning is:", round(yearly_take_home - current_yearly_take_home, 2))
print("=====")

print(calculations_list)

# figure out how to output to a CSV

calculatations_out = str(calculations_list)
telephony_out = "The weekly telephony payments are" + str(round(weekly_telephony, 2))
income_out = "your weekly income is:" + str( weekly_income)
take_home_out = "Weekly take home pay after taxes and National Insurance is roughly:" + str(round(weekly_take_home, 2))
monthly_earnings_out = "Monthly earnings after tax and expenses is roughly" + str(round(monthly_take_home, 2))
yearly_earnings_out = "Yearly earnings after tax and expenses is roughly" + str(round(yearly_take_home, 2))
difference_out = "The difference in current earning is:" + str( round(yearly_take_home - current_yearly_take_home, 2))

file = open("test_expenses_out.txt", "a")
file.write("Inputs were:")
file.write(calculatations_out)
file.write("=====")
file.write(telephony_out)
file.write(income_out)
file.write(take_home_out)
file.write(monthly_earnings_out)
file.write(yearly_earnings_out)
file.write(difference_out)
file.write("=====")