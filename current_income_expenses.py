'''
Created 29/11/2019

Create expenses calculator

@author: Richard Whittle
'''

import sys

# calculating the costs of commuting  and living away from home

# calculate the tax region and call the appropriate
def select_tax_region(input):
    try:
        i = int(input)
    except ValueError:
        print ("Please enter either 1 or 2, your tax region was not recognised, so is calculated as a non scottish region")

    if input == "1":
        print("selected UK, scotland")
        personal_tax_allowance(gross_pay)
        national_insurance(gross_pay)
        yearly_wages_scot(gross_pay)
    elif input == "2":
        print("selected UK, outside scotland")
        personal_tax_allowance(gross_pay)
        national_insurance(gross_pay)
        yearly_wages_uk_other(gross_pay)
    else:
        yearly_wages(gross_pay)

# define salary sacrifice conditions and return appropriate starter rates
def personal_tax_allowance(wages):
    ''' This block should be calculating the reduction in your personal allowance between 100k and 150k'''
    if (wages > 100000) and (wages < 150000):
        reduction = wages - 100000
        allowance_sacrifice = reduction / 2
    else:
        allowance_sacrifice = wages
    return allowance_sacrifice

# define the take home wages
## N.B. still having a calculation issue on the higher end taxes being grossly out, need to debug why, issue appears to be with the higher and top rates

def national_insurance(wages):
    '''Calculates and returns your national insurance payments '''
    if wages < 8632:
        national_insurance_rate = 0   
    elif wages < 41444: # calculats basic NI
        national_insurance_rate = (wages - 8632) * 0.12
    elif wages >= 41444: # Caclulates higher NI + full Basic NI ## full basic calc1 is 6000?
        national_insurance_rate = ((wages - 41444) * 0.02) + 3973
    print("national insurance is", national_insurance_rate)
    return national_insurance_rate

def yearly_wages_uk_other(wages):
    """This calulates your wages based on you living in the UK and outside of Scotland """  

    print("calculating UK other than scottish taxes") 
    national_insurance_rate = national_insurance(wages)
    print("Your salary  sacrifice if over 100,000 is, otherwise your wages are", personal_tax_allowance(wages))
    tax_bands = [8632, 12500, 50000, 150000]

    full_basic = (tax_bands[1] * 0.2) # basic rate at 20 % tax
    full_higher= (tax_bands[2] * 0.4) # higher rate at 40 % tax
    wages(tax_bands[3] * 0.41) # higher rate at 41 % allowance decreases


    if wages < tax_bands[0]: 
        after_tax_salary = wages
    elif wages < tax_bands[1]: # Only pay National Insurance
        after_tax_salary = wages - national_insurance_rate
    elif wages < tax_bands[2]: # Only pay basic rate at 20%
        taxes = (wages - tax_bands[1]) * 0.2 + national_insurance_rate
        after_tax_salary = wages - taxes
    elif wages < tax_bands[3]: # Only pay intermediate rate at 40%
        taxes = full_basic + ((wages - tax_bands[2]) * 0.4) + national_insurance_rate
        after_tax_salary = wages - taxes 
    elif wages >= tax_bands[3]: # Pay top rate tax
        taxes = full_basic + full_higher + (wages - tax_bands[3] * 0.41) + national_insurance_rate
        after_tax_salary = wages - taxes
    weekly_wages = round((after_tax_salary / 52.090714))
    return weekly_wages
  
def yearly_wages_scot(wages):
    """This calculates your wages based on you living in Scotland """  
    try:
        i = int(wages)
    except:
        print("You must enter your salary")

    national_insurance_rate = national_insurance(wages)
    print("Your salary  sacrifice if over 100,000 is, otherwise your wages are: ", personal_tax_allowance(wages))

    scottish_tax_bands = [8632, 12500, 14549, 24944, 43430, 150000]

    starter_wages = wages - (scottish_tax_bands[1] * 0.19)
    basic_wages = wages - ((scottish_tax_bands[2] * 20) / 100)
    intermediate_wages = wages - ((scottish_tax_bands[3] * 21) /100)
    higher_wages = wages - ((scottish_tax_bands[4] * 41) / 100)
    top_wages = wages - ((scottish_tax_bands[5] * 46) / 100)

    full_starter = (scottish_tax_bands[1] * 19) / 100 #    print("Full starter rate is", full_starter)
    full_basic = (scottish_tax_bands[2] * 20) / 100 #    print("Full basic rate is", full_basic)
    full_intermediate = (scottish_tax_bands[3] * 21) /100 #    print("Full intermediate rate is", full_intermediate)
    full_higher = (scottish_tax_bands[4] * 41) / 100 #    print("Full higher rate is",full_higher)

    if wages < scottish_tax_bands[0]: 
        taxes = national_insurance_rate
        after_tax_salary = wages

    elif wages < scottish_tax_bands[1]: # only pay NI       
        taxes = national_insurance_rate
        after_tax_salary = wages - national_insurance_rate

    elif wages < scottish_tax_bands[2]: # only pay starter rate
        taxes = national_insurance_rate
        after_tax_salary = starter_wages - taxes

    elif wages < scottish_tax_bands[3]: # paying basic rate
        taxes = full_starter + national_insurance_rate
        after_tax_salary = intermediate_wages - taxes

    elif wages < scottish_tax_bands[4]: # paying intermediate rates
        taxes = full_starter + full_basic + national_insurance_rate
        after_tax_salary = intermediate_wages - taxes

    elif wages < scottish_tax_bands[5]: # paying higher rate
        taxes = national_insurance(wages) + full_basic + full_intermediate + national_insurance_rate
        after_tax_salary = higher_wages - taxes

    elif wages > scottish_tax_bands[5]: # paying top rate
        taxes = full_starter + full_basic + full_intermediate + full_higher + national_insurance_rate
        after_tax_salary = top_wages - taxes

    weekly_wages = round(after_tax_salary / 52)
    print("your salary is", wages)
    print("Your taxes are:", taxes)
    print("your after tax salery is calculated on", after_tax_salary)
    return weekly_wages
    
def yearly_wages(wages):
    """This calculates with the default outside of scotland tax bands """     
    print("calculating UK other than scottish taxes") 
    national_insurance_rate = (wages - 8632) * 0.12
    tax_bands = [8632, 12500, 50000]

    if wages == "":
        after_tax_salary = 0
    elif wages < tax_bands[0]:
        after_tax_salary = wages
    elif wages < tax_bands[1]:        
        after_tax_salary = wages - national_insurance_rate
    elif wages < tax_bands[2]:
        basic_rate = (wages - tax_bands[1]) * 20 / 100
        after_tax_salary = wages - basic_rate - national_insurance_rate
    elif wages >= 50000:
        wages((wages - tax_bands[1]) * 20 / 100) + ((wages - tax_bands[2]) * 40 /100)
        after_tax_salary = wages - wagesnational_insurance_rate   
    weekly_wages = round((after_tax_salary / 52.090714))
    return weekly_wages

def test_wages_uk_other():
    """tests the calculations are correct based off of HMRC with no pension contributions selected with the most common tax code based in Scotland"""
    assert round(yearly_wages_uk_other(10000)) == 189
    assert round(yearly_wages_uk_other(12500)) == 231
    assert round(yearly_wages_uk_other(14550)) == 258
    assert round(yearly_wages_uk_other(24945)) == 394
#    assert yearly_wages_uk_other(43431) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in
#    assert yearly_wages_uk_other(150001) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in

# testing values against Scottish tax bands, needs to be rounded and figure out why there is a slight difference in the results
def test_wages_scot():
    """tests the calculations are correct based off of HMRC with no pension contributions selected with the most common tax code based in Scotland"""
    assert round(yearly_wages_scot(10000)) == 189
    assert round(yearly_wages_scot(12500)) == 231
    assert round(yearly_wages_scot(14550)) == 258
    assert round(yearly_wages_scot(24945)) == 394
#    assert round(yearly_wages_scot(43431)) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in
#    assert round(yearly_wages_scot(150001)) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in

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
        weekly_council_tax = 932.26 / 52.090714
    elif council_tax_calc == "A":
        weekly_council_tax = 1118.71 / 52.090714
    elif council_tax_calc == "B":
        weekly_council_tax = 1305.17 / 52.090714
    elif council_tax_calc == "C":
        weekly_council_tax = 1491.62 / 52.090714
    elif council_tax_calc == "D":
        weekly_council_tax = 1678.07 / 52.090714
    elif council_tax_calc == "E":
        weekly_council_tax = 2164.08 / 52.090714 
    elif council_tax_calc == "F":
        weekly_council_tax = 2646.65 / 52.090714
    elif council_tax_calc == "G":
        weekly_council_tax = 3,156.65 / 52.090714
    else:
        weekly_council_tax = 3911.36 / 52.090714
    return float(weekly_council_tax)
    print("Your weekly council tax payments at band", council_tax_calc, " are", round(weekly_council_tax, 2))

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
        
# Basis for differential wage calculation
current_wages = (int(input("What is your current salary? :")))

while True:
    try:
        gross_pay = (int(input("Enter the wage you wish to calculate: ")))
        break
    except:
        print("You must enter your salary as a numeric value")
        sys.exit(1)

select_tax_region = (input("If you live in Scotland press 1, if you live in the rest of the UK press 2: "))
if select_tax_region == '1':
    weekly_income = yearly_wages_scot(gross_pay)
    current_weekly_income = yearly_wages_scot(current_wages)
elif select_tax_region == '2':
    weekly_income = yearly_wages_uk_other(gross_pay)
    current_weekly_income = yearly_wages_uk_other(current_wages)
else:
    weekly_income = yearly_wages_uk_other(gross_pay)
    current_weekly_income = yearly_wages_uk_other(current_wages)

#test_wages_scot()

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


