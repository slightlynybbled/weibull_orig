import weibull

designer = weibull.Design(
    target_cycles=10000,
    reliability=0.9,
    confidence_level=0.90,
    expected_beta=1.5
)

# The 'test_cycles' parameter can be in any units.
# Days, weeks, hours, cycles, etc., so long
#   as the target unit is consistent
print(f'Minimum number of units for 10000 hour run: {designer.num_of_units(test_cycles=10000)}')
print(f'Minimum hours for 20 units: {designer.num_of_cycles(num_of_units=20)}')
