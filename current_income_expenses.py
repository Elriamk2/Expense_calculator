'''
Created 29/11/2019
Create expenses calculator
@author: Richard Whittle
'''

import sys
import re
#import test_exp_travel
from current_income_expenses import *

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
    while True:
        try:
            int(wages)
        except(ValueError):
            national_insurance_rate = 0
            #print("National Inurance Value Error ")
        except(TypeError):
            national_insurance_rate = 0
            print("National Inurance Type Error ")
        else:
            if wages < 8632:
                national_insurance_rate = 0   
            elif wages < 41444: # calculats basic NI
                national_insurance_rate = (wages - 8632) * 0.12
            elif wages >= 41444: # Caclulates higher NI + full Basic NI ## full basic calc1 is 6000?
                national_insurance_rate = ((wages - 41444) * 0.02) + 3973
            # print("national insurance is", national_insurance_rate)
        return round(national_insurance_rate / 52.090714)

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
    return (wages, taxes, after_tax_salary, weekly_wages)
  
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
    return (wages, taxes, after_tax_salary, weekly_wages)

#purge the following as it should no longer be needed
'''    
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
'''