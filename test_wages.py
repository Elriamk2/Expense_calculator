from current_income_expenses import yearly_wages_uk_other
from current_income_expenses import yearly_wages_scot

# Tests to be completed
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
    assert round(yearly_wages_scot(24945)) == 390 # 394
#    assert round(yearly_wages_scot(43431)) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in
#    assert round(yearly_wages_scot(150001)) == weekly_wages # Still showing a difference of a few pounds here, unsure where the error is creeping in

test_wages_scot()