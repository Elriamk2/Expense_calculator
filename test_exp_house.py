# test home expenses

# Import assets
from calculate_expenses import housing_payments
from calculate_expenses import council_tax_band

# Test Housing costs (mortgage)
test_mortgage_nil = housing_payments()
test_mortgage_low = housing_payments(50)
test_mortgage_medium = housing_payments(500)
test_mortgage_high = housing_payments(10000)
test_mortgage_alpha = housing_payments("four hundred")
test_mortgage_negative = housing_payments(-100)

assert test_mortgage_nil[1] == 0
assert test_mortgage_low[1] == 12.5
assert test_mortgage_medium[1] == 125
assert test_mortgage_high[1] == 2500
assert test_mortgage_alpha[1] == 0
assert test_mortgage_negative[1] == 0 

# test council_tax_band
test_council_tax_lowercase = council_tax_band("a")
test_council_tax_uppercase = council_tax_band("B")
test_council_tax_float = council_tax_band(1491.62)
test_council_tax_nil = council_tax_band(0)
test_council_tax_negative = council_tax_band(-932.26)
test_council_tax_invalid = council_tax_band("umm")

assert test_council_tax_lowercase[1] == 21.48
assert test_council_tax_uppercase[1] == 25.06
assert test_council_tax_float[1] == 0
assert test_council_tax_nil[1] == 0
assert test_council_tax_negative[1] == 0
assert test_council_tax_invalid[1] == 0
