##### 
# Author: Richard Whittle
#####

# Expense_calculator
 designed to help calculate take home pay, for current and future jobs. This is intended to assist with life planning and is not a definitive solution, the completed solution should however give an idea of potential changes in income due to changes in expenses or earnings.
 
 (or it will soon enough.)

29/11/2019

 Tasks completed:
 Tested underlying script and created some unit tests 29/11/2019

 Tasks to be done:

 * Seperate inputs into current_income_expenses and planned_income_expenses
 * Clean up expenses_calc to use returns rather than globals
 * Impliment new import methods rather than using input to update the raw files

05/12/2019

Created stable branch as base functions are working with an error in the higher end calculations leading to a difference of 10's of pounds in higher end values. However as this is not really for reelase and is mainly to test my development and maintenance for python I feel it is an acceptable bug. This will be reviewed later.

2019 12 29

Uodated error handling in the unit tests, 
Breaking unit tests out to function sepecific files

To be done:
* amend the outputs to be handled elsewhere so the caclulations no longer generate spurius text whilst doing unit tests.

2020 01 04
Branch stable and passing tests, closed 3 suggestions on project board, outstanding issues to be resolved include high end calculations for taxes, otherwise calculations are good.
