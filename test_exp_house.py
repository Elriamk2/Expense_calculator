# test home expenses

# Import assets
from calculate_expenses import housing_payments
from calculate_expenses import council_tax_band

# Test Housing costs (mortgage)
test_mortgage_nil = 0
test_mortgage_low = 50
test_mortgage_medium = 500
test_mortgage_high = 10000
test_mortgage_alpha = "four hundred"
test_mortgage_negative = -100

assert housing_payments(test_mortgage_nil) == 0
assert housing_payments(test_mortgage_low) == 12.5
assert housing_payments(test_mortgage_medium) == 125
assert housing_payments(test_mortgage_high) == 2500
assert housing_payments(test_mortgage_negative) == 0
assert housing_payments(test_mortgage_alpha) == 0 

# test council_tax_band
test_council_tax_lower = "a"
test_council_tax_upper = "B"
test_council_tax_float = 1491.62
test_council_tax_nil = 0
test_council_tax_negative = -932.26
test_council_tax_invalid = "Gimmie rent"

assert council_tax_band(test_council_tax_lower) == 21.48
assert council_tax_band(test_council_tax_upper) == 25.06
assert council_tax_band(test_council_tax_nil) == 0
assert council_tax_band(test_council_tax_negative) == 0
