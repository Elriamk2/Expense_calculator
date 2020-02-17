'''
Created 29/11/2019
Create expenses calculator
@author: Richard Whittle
'''

import sys
import re

# check if running as __main__
if __name__ == "__main__":
    gross_pay = 0
    select_tax_region(input = 0)
    personal_tax_allowance(wages = 0)
    national_insurance(wages = 0)
    yearly_wages_uk_other(wages = 0)
    yearly_wages_scot(wages = 0)
    additional_income(other = 0)

class national_insurance:
    def __init__(self, gross_pay):
        self.gross_pay = gross_pay

    def __repr__(self):
        return f({self.gross_pay})

# calculate the tax region and call the appropriate
def select_tax_region(input):
    try:
        input = int(input)
    except ValueError:
        input = 2
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
        yearly_wages_uk_other(gross_pay)

# define salary sacrifice conditions and return appropriate starter rates
def personal_tax_allowance(wages = 0):
    ''' This block should be calculating the reduction in your personal allowance between 100k and 150k'''
    while True:
        try:
            wages = int(wages)
        except TypeError:
            allowance_sacrifice = 0
        else:
            if (wages > 100000) and (wages < 150000):
                reduction = wages - 100000
                allowance_sacrifice = reduction / 52.090714
            else:
                allowance_sacrifice = wages
        return allowance_sacrifice

# define the take home wages
## N.B. still having a calculation issue on the higher end taxes being grossly out, need to debug why, issue appears to be with the higher and top rates

def national_insurance(wages = 0):
    '''Calculates and returns your national insurance payments '''
    while True:
        try:
            wages = int(wages)
        except(ValueError, TypeError):
            national_insurance_rate = 0
            wages = 0
            # print("National Inurance Value Error ")
        finally:
            if wages < 8632:
                national_insurance_rate = 0   
            elif wages < 41444: # calculats basic NI
                national_insurance_rate = (wages - 8632) * 0.12
            elif wages >= 41444: # Caclulates higher NI + full Basic NI ## full basic calc1 is 6000?
                national_insurance_rate = ((wages - 41444) * 0.02) + 3973
            # print("national insurance is", national_insurance_rate)
        return(national_insurance_rate, round(national_insurance_rate / 52.090714))

def yearly_wages_uk_other(wages = 0):
    """This calulates your wages based on you living in the UK and outside of Scotland """  
    while True:
        try:
            wages = int(wages)
        except(ValueError):
            wages = 0
            taxes = 0
            after_tax_salary = 0
            weekly_wages = 0
        else:
            # print("calculating UK other than scottish taxes") 
            national_insurance_rate = national_insurance(wages)
            # return print("Your salary  sacrifice if over 100,000 is, otherwise your wages are", personal_tax_allowance(wages))
            tax_bands = [8632, 12500, 50000, 150000]

            full_basic = (tax_bands[1] * 0.2) # basic rate at 20 % tax
            full_higher = (tax_bands[2] - tax_bands[1]) * 0.4 # higher rate at 40 % tax
            
            if wages <= tax_bands[0]: # Only pay National Insurance
                taxes = national_insurance_rate[0]
                after_tax_salary = wages
            elif wages <= tax_bands[1]: # Only pay National Insurance
                taxes = national_insurance_rate[0]
                after_tax_salary = wages - taxes
            elif wages <= tax_bands[2]: # Only pay basic rate at 20%
                taxes = ((wages - tax_bands[1]) * 0.2) + national_insurance_rate[0]
                after_tax_salary = wages - taxes
            elif wages <= tax_bands[3]: # Only pay intermediate rate at 40%
                taxes = full_basic + ((wages - tax_bands[2]) * 0.4) + national_insurance_rate[0]
                after_tax_salary = wages - taxes
            elif wages >= tax_bands[3]: # pay additional rate at 45%
                #taxes = full_basic + full_higher + additional_rate + national_insurance_rate[0]
                taxes = full_basic + full_higher + ((wages - tax_bands[3]) * .45) + national_insurance_rate[0]
                after_tax_salary = wages - taxes
            weekly_wages = round((after_tax_salary / 52)) #.090714
            taxes = round(wages - after_tax_salary, 2)
        return (wages, taxes, after_tax_salary, weekly_wages)
  
def yearly_wages_scot(wages = 0):
    """This calculates your wages based on you living in Scotland """  
    while True:
        try:
            wages = int(wages)
        except(ValueError):
            wages = 0
            taxes = 0
            after_tax_salary = 0
            weekly_wages = 0
        else:

            national_insurance_rate = national_insurance(wages)
            # return some other way? print("Your salary  sacrifice if over 100,000 is, otherwise your wages are: ", personal_tax_allowance(wages))

            scottish_tax_bands = [8632, 12500, 14549, 24944, 43430, 150000]

            starter_wages = wages - (scottish_tax_bands[1] * 0.19)
            basic_wages = wages - (scottish_tax_bands[2] * 0.2)
            intermediate_wages = wages - (scottish_tax_bands[3] * 0.21)
            higher_wages = wages - (scottish_tax_bands[4] * 0.41 / 100)
            top_wages = wages - (scottish_tax_bands[5] * 0.46)

            full_starter = scottish_tax_bands[1] * 0.19 #    print("Full starter rate is", full_starter)
            full_basic = scottish_tax_bands[2] * 0.2 #    print("Full basic rate is", full_basic)
            full_intermediate = scottish_tax_bands[3] * 0.21 #    print("Full intermediate rate is", full_intermediate)
            full_higher = scottish_tax_bands[4] * 0.41 #    print("Full higher rate is",full_higher)

            if wages < scottish_tax_bands[0]: 
                taxes = national_insurance_rate[0]
                after_tax_salary = wages

            elif wages < scottish_tax_bands[1]: # only pay NI       
                taxes = national_insurance_rate[0]
                after_tax_salary = wages - taxes

            elif wages < scottish_tax_bands[2]: # only pay starter rate
                taxes = national_insurance_rate[0]
                after_tax_salary = starter_wages - taxes

            elif wages < scottish_tax_bands[3]: # paying basic rate
                taxes = full_starter + national_insurance_rate[0]
                after_tax_salary = intermediate_wages - taxes

            elif wages < scottish_tax_bands[4]: # paying intermediate rates
                taxes = full_starter + full_basic + national_insurance_rate[0]
                after_tax_salary = intermediate_wages - taxes

            elif wages < scottish_tax_bands[5]: # paying higher rate
                taxes = full_basic + full_intermediate + national_insurance_rate[0]
                after_tax_salary = higher_wages - taxes

            elif wages > scottish_tax_bands[5]: # paying top rate
                taxes = full_starter + full_basic + full_intermediate + full_higher + national_insurance_rate[0]
                after_tax_salary = top_wages - taxes

            weekly_wages = round(after_tax_salary / 52) # for full year it would be an additional .090714
            taxes = round(wages - after_tax_salary, 2)
        return (wages, taxes, after_tax_salary, weekly_wages)

def additional_income(other):
    "This calculates your additional income streams"
    while True:
        try:
            extra_income = float(other) / 4.35
        except (TypeError, ValueError):
            extra_income = float(0)
        return extra_income
            