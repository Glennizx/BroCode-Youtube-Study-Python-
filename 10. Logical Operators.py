# Logical operators = evaluate multiple conditions (or, and, not)
#            or = at least one condition must be True
#            and = both conditions must be True
#            not = inverts the condition (not False, not True)


temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")

elif temp <