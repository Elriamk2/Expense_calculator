'''
Created 29/11/2019

Create expenses calculator

@author: Richard Whittle
'''

# calculating the costs of commuting  and living away from home

# calculate the tax region and call the appropriate
def select_tax_region(input):
    if input == "1":
        print("selected UK, scotland")
        yearly_wages_scot(gross_pay)
    elif input == "2":
        print("selected UK, outside scotland")
        yearly_wages_uk_other(gross_pay)
    else:
        print("your tax region was not recognised")
        yearly_wages(gross_pay)

# define the take home wages

def yearly_wages_uk_other(wages):
    """This calulates your wages based on you living in the UK and outside of Scotland """    
    print("calculating UK other than scottish taxes") 
    national_insurance_rate = (wages - 8632) * 12 / 100
    if wages == "":
            print("You must enter a salary")
    elif wages < 8632:
        after_tax_salary = wages
    elif (wages < 12500):        
        after_tax_salary = wages - national_insurance_rate
    elif wages < 50000:
        basic_rate = (wages - 12500) * 20 / 100
        after_tax_salary = wages - basic_rate - national_insurance_rate
    elif wages >= 50000:
        higher_rate = ((wages - 12500) * 20 / 100) + ((wages - 50000) * 40 /100)
        after_tax_salary = wages - higher_rate - national_insurance_rate   
    weekly_wages = round((after_tax_salary / 52))
    return weekly_wages
  
def yearly_wages_scot(wages):
    """This calulates your wages based on you living in Scotland """  
    national_insurance_rate = (wages - 8632) * 12 / 100
    if wages == "":
            print("You must enter a salary")
    elif wages <= 8632: 
        after_tax_salary = wages
    elif (wages < 12500): # only pay NI       
        after_tax_salary = wages - national_insurance_rate
    elif (wages <= 14550): # only pay starter rate
        starter_rate = (wages - 12500) * 19 / 100
        after_tax_salary = wages - starter_rate - national_insurance_rate
    elif wages < 24944:
        starter_rate = (wages - 12500) * 19 / 100
        basic_rate = (wages - 14549) * 20 / 100
        after_tax_salary = wages - starter_rate - basic_rate - national_insurance_rate
    elif wages <= 43430:
        starter_rate = (wages - 12500) * 19 / 100
        basic_rate = (wages - 14549) * 20 / 100
        intermediate_rate = (wages - 24944) * 21 /100
        after_tax_salary = wages - starter_rate - basic_rate - intermediate_rate - national_insurance_rate
    elif wages <= 150000:
        starter_rate = (wages - 12500) * 19 / 100
        basic_rate = (wages - 14549) * 20 / 100
        intermediate_rate = (wages - 24944) * 21 /100
        higher_rate = (wages - 43431) * 41 / 100
        after_tax_salary = wages - starter_rate - basic_rate - intermediate_rate - higher_rate - national_insurance_rate
    elif wages > 150000:
        starter_rate = (wages - 12500) * 19 / 100
        basic_rate = (wages - 14549) * 20 / 100
        intermediate_rate = (wages - 24944) * 21 /100
        higher_rate = (wages - 43431) * 41 / 100
        top_rate = (wages - 150000) * 46 / 100
        after_tax_salary = wages - starter_rate - basic_rate - intermediate_rate - higher_rate - top_rate - national_insurance_rate
    weekly_wages = round((after_tax_salary / 52))
    #print("Scottish weekly wages ", weekly_wages)
    return weekly_wages
    
def yearly_wages(wages):
    """This calulates with the default outside of scotland tax bands """     
    if wages == "":
            print("You must enter a salary")
    elif wages < 8632:
        after_tax_salary = wages
    elif (wages < 12500):
        national_insurance_rate = (wages - 8632) * 12 / 100
        after_tax_salary = wages - national_insurance_rate
    elif wages < 50000:
        basic_rate = (wages - 12500) * 20 / 100
        national_insurance_rate = (wages - 8632) * 12 / 100
        after_tax_salary = wages - basic_rate - national_insurance_rate
    elif wages >= 50000:
        higher_rate = ((wages - 12500) * 20 / 100) + ((wages - 50000) * 40 /100)
        national_insurance_rate = (wages - 8632) * 12 / 100
        after_tax_salary = wages - higher_rate - national_insurance_rate   
    weekly_wages = round((after_tax_salary / 52))
    return weekly_wages

def test_wages_uk_other():
    """tests the calculations are correct based off of HMRC with no pension contributions selected with the most common tax code based in Scotland"""
    assert yearly_wages_uk_other(10000) == 189.15076923076924
#    assert yearly_wages_uk_other(12500) == weekly_wages
#    assert yearly_wages_uk_other(14550) == weekly_wages
#    assert yearly_wages_uk_other(24945) == weekly_wages
#    assert yearly_wages_uk_other(43431) == weekly_wages
#    assert yearly_wages_uk_other(150001) == weekly_wages

# testing values against Scottish tax bands, needs to be rounded and figure out why there is a slight difference in the results
def test_wages_scot():
    """tests the calculations are correct based off of HMRC with no pension contributions selected with the most common tax code based in Scotland"""
    assert yearly_wages_scot(10000) == 189.15076923076924
    assert yearly_wages_scot(12500) == 231.45846153846153
#    assert yearly_wages_scot(14550) == 258.2661538461538
#    assert yearly_wages_scot(24945) == 394.2007692307692
#    assert yearly_wages_scot(43431) == weekly_wages
#    assert yearly_wages_scot(150001) == weekly_wages

# Travel Expenses
def car_travel_per_trip(distance):
    """Calculates the cost of travel based on a 45p / mile Millage allowance"""
    # take the distance input and multiply that by 45p
    car_allowance = (distance * 45)
    if distance > 0:
        weekly_car_allowance = car_allowance / 100
        print("Your weekly car maintenace allowance is:", weekly_car_allowance)
    else:
        print("You have no car milage costs")
        weekly_car_allowance = 0
    return weekly_car_allowance

def train_ticket_return(train_ticket_return):
    """Calculates the weekly costs of a train ticket """       
    global weekly_train_allowance
    if train_ticket_return == "":
        print("You have no train expenses")
        weekly_train_allowance = 0
    elif train_ticket_return == 0:
        print("You have no train expenses")
        weekly_train_allowance = 0
    elif train_ticket_return > 0:
        weekly_train_allowance = (train_ticket_return * 5)
        print("Your weekly train ticket costs are:", weekly_train_allowance)
    else:
        print("You have no train expenses")
        weekly_train_allowance = 0

# Housing costs
def housing_payments(housing_payments):
    """Calculates the weekly and yearly monthly payments based on the monthly costs"""
    global weekly_housing_costs
    if housing_payments > 0:
        weekly_housing_costs = (housing_payments / 4)
        print("Your weekly housing costs are", weekly_housing_costs)
    else:
        print("You have no mortgage expenses")
        weekly_housing_costs = 0

def council_tax_band(council_tax_band):
    council_tax_calc = council_tax_band.upper()
    """Calculates your council tax based on the  """
    if council_tax_calc == "":
        print("You have not entered any council tax and the calculcation assumes this is 0")
        weekly_council_tax = 0
    elif council_tax_band =="0":
        print("You are not currently paying council tax")
        weekly_council_tax = 0
    elif council_tax_calc == "A*":
        weekly_council_tax = 932.26 / 52
    elif council_tax_calc == "A":
        weekly_council_tax = 1118.71 / 52
    elif council_tax_calc == "B":
        weekly_council_tax = 1305.17 / 52
    elif council_tax_calc == "C":
        weekly_council_tax = 1491.62 / 52
    elif council_tax_calc == "D":
        weekly_council_tax = 1678.07 / 52
    elif council_tax_calc == "E":
        weekly_council_tax = 2164.08 / 52 
    elif council_tax_calc == "F":
        weekly_council_tax = 2646.65 / 52
    elif council_tax_calc == "G":
        weekly_council_tax = 3,156.65 / 52
    else:
        weekly_council_tax = 3911.36 / 52
    return int(weekly_council_tax)
    print("Your weekly council tax payments at band", council_tax_calc, " are", round(weekly_council_tax_payments, 2))

def monthly_electricity_bill(monthly_electric_bill):
    """Calculates the weekly costs of your electric bills based in £ based on a 4.45 week cycle"""
    if monthly_electric_bill == 0:
        weekly_electric_bill = 0
        print("You have no electic bills calculated")
    elif monthly_electric_bill > 0:
        weekly_electric_bill = monthly_electric_bill / 4.45
        print("Your weekly electric bill is:", weekly_electric_bill)
    else:
        weekly_electric_bill = 0
        print("You have entered an invalid figure")
    return weekly_electric_bill

def monthly_telephony_bill(telephony):
    """Calculates the costs of you telephone bills in £ based on a 4.45 week cycle"""
    if telephony == 0:
        telephony_bill = 0
    elif telephony > 0:
        telephony_bill = telephony / 4.45
        print("Your Weekly telephony bill is", telephony_bill)
    else:
        telephony_bill = 0
        print("You have entered an invalid figure")
    return telephony_bill    
        
#current_gross_pay = (30401)
gross_pay = (int(input("Enter the wage you wish to calculate: ")))
select_tax_region(input("If you live in Scotland press 1, if you live in the rest of the UK press 2: "))
if (input) == "1":
    weekly_income = yearly_wages_scot(gross_pay)
elif (input) == "2":
        weekly_income = yearly_wages_uk_other(gross_pay)
else:
    weekly_income = yearly_wages(gross_pay)

#print(" testing the weekly income function call", weekly_income)

# test_wages_scot()

# define the travel to work / secondary location costs
car_distance = (int(input("What is the return trip distance? If you are not using a car enter 0: ")))
car_trips = (int(input("How many trips do you make? If you are not using a car enter 0: ")))
calculate_car_travel = car_distance * car_trips

weekly_car_payments = car_travel_per_trip(calculate_car_travel)

# define the train travel costs
# train_ticket_return(4.70)
train_ticket_return(float(input("How much does your ticket cost? Enter 0 if not using a train: ")))
#current_train_ticket_return(0)

# Calculate housing costs, council tax band should be entered as a string
# council_tax_band("b")
council_tax_assesment = input("What council tax band is your house? Enter 0 if you are not paying council tax: ")
weekly_council_payments = int(council_tax_band(council_tax_assesment))
# housing_payments(156)
housing_payments(int(input("How much is your mortgage or rent? Enter 0 if you are not paying these: ")))

# monthly_electricity_bill(55)
weekly_electric_bill = monthly_electricity_bill(int(input("How much will you be paying per month for electricity? If no electic bill enter 0: ")))
#current_monthly_electricity_bill(699)

# monthly_broadband = 32.99
weekly_telephony = int(input("How much will you pay for telephony services monthly? If you are not paying for these enter 0: "))
monthly_telephony_bill(weekly_telephony)



# calculate the weekly outgoings
weekly_take_home = weekly_income - weekly_car_payments - weekly_council_payments - weekly_housing_costs - weekly_electric_bill - weekly_telephony # - weekly_gas_bill
monthly_take_home = weekly_take_home * 4
yearly_take_home = weekly_take_home * 52

# print all outputs
print("=====")
print("The weekly telephony payments are", round(weekly_telephony, 2))
print("your weekly income is:", weekly_income)
print("Weekly take home pay with taxes and National Insurance is roughly:", round(weekly_take_home, 2))
print("Monthly earnings after tax and expenses is roughly", round(monthly_take_home, 2))
print("Yearly earnings after tax and expenses is roughly", round(yearly_take_home, 2))
print("The difference in current earning is:", round(yearly_take_home - 21105.84, 2))
print("=====")


