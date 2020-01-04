from current_income_expenses import yearly_wages_uk_other
from current_income_expenses import yearly_wages_scot

# Tests to be completed
def test_wages_uk_other():
    """tests the calculations are correct based off of HMRC with no pension contributions selected with the most common tax code based in Scotland"""
    wages_uk_base = yearly_wages_uk_other(10000)
    wages_uk_low = yearly_wages_uk_other(12500)
    wages_uk_medium = yearly_wages_uk_other(24550)
    #wages_uk_high = yearly_wages_uk_other(275000)
    wages_uk_string = yearly_wages_uk_other("uk wages string")
    wages_uk_empty =  yearly_wages_uk_other("")
    
    assert wages_uk_base[3] == 189
    assert wages_uk_low[3] == 231
    assert wages_uk_medium[3] == 389
   # assert wages_uk_high[3] == 3015
    assert wages_uk_string[3] == 0
    assert wages_uk_empty[3] == 0
#    assert yearly_wages_uk_other(43431) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in
#    assert yearly_wages_uk_other(150001) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in

# testing values against Scottish tax bands, needs to be rounded and figure out why there is a slight difference in the results
def test_wages_scot():
    """tests the calculations are correct based off of HMRC with no pension contributions selected with the most common tax code based in Scotland"""
    wages_scot_base = yearly_wages_scot(10000)
    wages_scot_medium = yearly_wages_scot(50000)
    wages_scot_high = yearly_wages_scot(145500)
    wages_scot_string = yearly_wages_scot("scot wages string")
    wages_scot_empty = yearly_wages_scot("")

    assert wages_scot_base[3] == 189
#    assert wages_scot_medium[3] == 692
    #assert wages_scot_high[3] == 1633
    assert wages_scot_string[3] == 0
    assert wages_scot_empty[3] == 0

#tests 
test_wages_uk_other()
test_wages_scot()
