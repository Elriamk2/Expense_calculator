'''
Created 29/11/2019
Create expenses calculator
@author: Richard Whittle
'''

#from expense_calc_inputs import car_travel_per_trip
#from current_income_expenses import *
#from current_income_expenses import housing_payments
#from current_income_expenses import council_tax_band
#from current_income_expenses import monthly_electricity_bill
#from current_income_expenses import monthly_telephony_bill

# calculating the costs of commuting  and living away from home

# Travel Expenses
def car_travel_per_trip(distance = 0):
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

def train_ticket_return(train_ticket_return = 0, train_trips = 0):
    """Calculates the weekly costs of a train ticket """
    if train_ticket_return == "":
        print("You have no train expenses")
        weekly_train_allowance = 0
    elif train_ticket_return == 0:
        print("You have no train expenses")
        weekly_train_allowance = 0
    elif train_ticket_return > 0:
        weekly_train_allowance = (train_ticket_return * train_trips)
        print("Your weekly train ticket costs are:", weekly_train_allowance)
    else:
        print("You have no train expenses")
        weekly_train_allowance = 0
        weekly_train_allowance = train_ticket_return
    return weekly_train_allowance

# Housing costs
def housing_payments(housing_payments = 0):
    """Calculates the weekly and yearly monthly payments based on the monthly costs""" 
    while True:
        try:
            check = housing_payments
            check = float(housing_payments)
        except (TypeError, ValueError):
            weekly_housing_costs = 0
            #print("invalid value used, housing costs calculated as 0")
        else:
            if housing_payments > 0:
                weekly_housing_costs = (housing_payments / 4)
                #print("Your weekly housing costs are", weekly_housing_costs)
            else:
                #print("You have no housing expenses")
                weekly_housing_costs = 0
        #print("Your weekly housing costs are", weekly_housing_costs) Handle this in the input file outputs?
        return weekly_housing_costs

def council_tax_band(council_tax_band = 0):
    """Calculates your council tax based on the  """
    while True:
        try:
            council_tax_calc = council_tax_band.upper()
        except (AttributeError, TypeError):
            weekly_council_tax = 0
        #    print("Invalid tax band used")
        else:
            if council_tax_band =="0":
                #print("You are not currently paying council tax")
                weekly_council_tax = 0
            elif council_tax_calc.upper() == "A*":
                weekly_council_tax = 932.26 / 52.090714
            elif council_tax_calc.upper() == "A":
                weekly_council_tax = 1118.71 / 52.090714
            elif council_tax_calc.upper() == "B":
                weekly_council_tax = 1305.17 / 52.090714
            elif council_tax_calc.upper() == "C":
                weekly_council_tax = 1491.62 / 52.090714
            elif council_tax_calc.upper() == "D":
                weekly_council_tax = 1678.07 / 52.090714
            elif council_tax_calc.upper() == "E":
                weekly_council_tax = 2164.08 / 52.090714 
            elif council_tax_calc.upper() == "F":
                weekly_council_tax = 2646.65 / 52.090714
            elif council_tax_calc.upper() == "G":
                weekly_council_tax = 3,156.65 / 52.090714
            else:
                weekly_council_tax = 3911.36 / 52.090714
#    calculations_list[6] = council_tax_band
        return round(weekly_council_tax, 2)
    #print("Your weekly council tax payments at band", council_tax_calc, " are", weekly_council_tax)
    #Handle Outputs elsewhere

def monthly_electricity_bill(electric_bill = 0):
    """Calculates the weekly costs of your electric bills based in £ based on a 4.45 week cycle"""
    while True:
        try:
            float(electric_bill)
        except (ValueError, TypeError):
            weekly_electric_bill = 0
            #print("typeError encountered")
        else:
            if electric_bill == 0:
                weekly_electric_bill = 0
        #print("You have no electic bills calculated")
            elif electric_bill > 0:
                weekly_electric_bill = electric_bill / 4.45
        #print("Your weekly electric bill is:", weekly_electric_bill)
            else:
                electric_bill = 0
        #print("You have entered an invalid figure")
                weekly_electric_bill = electric_bill
        return round(weekly_electric_bill, 2)

def monthly_gas_bill(gas = 0):
    '''Calculate your weekly Gas bills in £ based on 4.45 week per month'''
    while True:
        try:
            float(gas)
        except (ValueError, TypeError):
            gas_bill = 0
            #print("Gas TypeError")
        else:
            if gas == 0:
                gas_bill = 0
            elif gas > 0:
                gas_bill = gas /4.45
            else:
                gas_bill = 0
        return round(gas_bill, 2)

def monthly_telephony_bill(telephony = 0):
    """Calculates the costs of you telephone bills in £ based on a 4.45 week cycle"""
    while True:
        try:
            float(telephony)
        except (ValueError, TypeError):
            telephony_bill = 0
            #print("typeError Telephony encountered")
        else:
            if telephony == 0:
                telephony_bill = 0
            elif telephony > 0:
                telephony_bill = telephony / 4.45
            #print("Your Weekly telephony bill is", telephony_bill)
            else:
                telephony_bill = 0
                #print("Telephony, you have entered 0")
                #telephony_bill = telephony
        return round(telephony_bill, 2)
