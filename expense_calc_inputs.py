from current_income_expenses import *
from calculate_expenses import *


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
        gross_pay = int((input("Enter the wage you wish to calculate: ")))
        calculations_list[0] = gross_pay
        break
    except:
        print("value not recognised, no salary entered")
        calculations_list[0] = 0
    finally:
        calculations_list[1] = (input("If you live in Scotland press 1, if you live in the rest of the UK press 2: "))
        if calculations_list[1] == '1':
            weekly_income = yearly_wages_scot(gross_pay)
            current_weekly_income = yearly_wages_scot(calculations_list[1])
        elif calculations_list[1] == '2':
            weekly_income = yearly_wages_uk_other(gross_pay)
            current_weekly_income = yearly_wages_uk_other((float(calculations_list[0])))
            wages_list = yearly_wages_uk_other()
        else:
            calculations_list[1] = 0
            weekly_income = yearly_wages_uk_other(gross_pay)
            current_weekly_income = yearly_wages_uk_other((float(calculations_list[0])))
            wages_list = yearly_wages_uk_other()
        print("Your input wages were: ", weekly_income[0], " ,your taxes are calculated as: ", weekly_income[1], ", your after tax salary is: ", weekly_income[2])
        weekly_wages = weekly_income[3]
        

    

# define the travel to work / secondary location costs
calculations_list[1] = (input("What is the return trip distance? If you are not using a car enter 0: "))
calculations_list[2] = (input("How many trips do you make? If you are not using a car enter 0: "))
calculate_car_travel = calculations_list[2] * calculations_list[3]
# calculations_list[2] = car_distance
# calculations_list[3] = car_trips

weekly_car_payments = car_travel_per_trip(calculate_car_travel)

# define the train travel costs
# train_ticket_return(4.70)
calculations_list[3] = input("How many return train trips do you take per week? Enter 0 if not using a train: ")
calculations_list[4] = input("How much does your train ticket cost? Enter 0 if not using a train: ")
#calculations_list[4] =  train_trips_per_week
weekly_train_costs = train_ticket_return(calculations_list[3], calculations_list[4])


# Calculate housing costs, council tax band should be entered as a string
# council_tax_band("b")
calculations_list[6] = input("What council tax band is your house? Enter 0 if you are not paying council tax: ")
council_payments = council_tax_band(calculations_list[6])
weekly_council_payments = council_payments[1]

#calculations_list[6] = council_tax_assesment(council_tax_assesment)

# housing_payments(156)
calculations_list[7] = input("How much is your mortgage or rent? Enter 0 if you are not paying these: ")
housing_payments = housing_payments(calculations_list[7])
weekly_housing_costs = housing_payments[1]

# monthly_electricity_bill(55)
calculations_list[8] = monthly_electricity_bill(input("How much will you be paying per month for electricity? If no electic bill enter 0: "))
electricity_payments = monthly_electricity_bill(calculations_list[8])
weekly_electric_bill = electricity_payments[1]

# monthly_gas_bill 
calculations_list[9] = monthly_electricity_bill(input("How much will you be paying per month for gas or oil? If no electic bill enter 0: "))
gas_payments = monthly_gas_bill(calculations_list[9])
weekly_gas_bill = gas_payments[1]

# monthly_broadband = 32.99
calculations_list[9] =input("How much will you pay for telephony services monthly? If you are not paying for these enter 0: ")
# monthly_telephony_bill(float(weekly_telephony))
weekly_telephony = monthly_telephony_bill(calculations_list[9])

#additional income streams
additional_monthly_income = float(input("Enter any additional monthly income, if none, enter 0: "))

# calculate the weekly outgoings
weekly_take_home = weekly_wages - weekly_car_payments - weekly_council_payments - weekly_train_costs - weekly_housing_costs - weekly_electric_bill - weekly_telephony + (additional_monthly_income / 4.35) - weekly_gas_bill
session_outs = [weekly_wages, weekly_car_payments, weekly_council_payments, weekly_train_costs, weekly_housing_costs, weekly_electric_bill, weekly_telephony, (additional_monthly_income / 4.35), weekly_gas_bill]
monthly_take_home = weekly_take_home * 4.35
yearly_take_home = weekly_take_home * 52.1
# next iteration calculate and diff current_yearly_take_home = current_weekly_income * 52.1

# # Handle wages outputs:
# print("Your salary is ", gross_pay[0])
# print("Your taxes are ", gross_pay[1])

# print all outputs
print("=====")
print("The weekly telephony payments are: ", weekly_telephony)
print("your weekly income is: ", weekly_take_home)
print("Weekly take home pay after expenses is roughly: ", round(weekly_take_home, 2))
print("Monthly earnings after tax and expenses is roughly: ", round(monthly_take_home, 2))
print("Yearly earnings after tax and expenses is roughly: ", round(yearly_take_home, 2))
# next iteration print("The difference in current earning is:", round(yearly_take_home - current_yearly_take_home, 2))
print("=====")

print(calculations_list)

# figure out how to output to a CSV

calculatations_out = str(calculations_list)
telephony_out = "The weekly telephony payments are: " + str(round(weekly_telephony, 2)) + "\n"
# handled earlier? income_out = "your weekly income is: " + str(weekly_income) + "\n"
take_home_out = "Weekly take home pay after taxes and National Insurance is roughly: " + str(round(weekly_take_home, 2)) + "\n"
monthly_earnings_out = "Monthly earnings after tax and expenses is roughly: " + str(round(monthly_take_home, 2)) + "\n"
yearly_earnings_out = "Yearly earnings after tax and expenses is roughly: " + str(round(yearly_take_home, 2)) + "\n"
# next iteration difference_out = "The difference in current earning is: " + str( round(yearly_take_home - current_yearly_take_home, 2) ) + "\n"

expense_write = open("test_expenses_out.txt", "a")
expense_write.write

expense_write.write("Inputs were: \n")
expense_write.write(calculatations_out)
expense_write.write("The Outputs for this are: \n")
expense_write.write(session_outs)
expense_write.write("\n ===== \n")
expense_write.write(telephony_out)
expense_write.write(yearly_earnings_out)
expense_write.write(take_home_out)
expense_write.write(monthly_earnings_out)
expense_write.write(yearly_earnings_out)
# next iteration file.write(difference_out)
expense_write.write("\n ===== \n")
expense_write.close()