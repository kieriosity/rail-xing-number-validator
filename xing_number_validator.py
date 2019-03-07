import re


def crossing_number_validation(xn):
    """
    The crossing_validator function takes a crossing input variable and then
    calculates if the value is valid.

    Calculating a valid crossing number:

    Example crossing number:  836597H

    Step 1. Compute the Total Numeric Value
        = [(8x1) + (3x2) + (6x3) + (5x4) + (9x5) + (7x6)]
        = (8 + 6 + 18 + 20 + 45 + 42)
        = 139
    Step 2. Find Remainder for the Alpha Code.
        = 139 - (subtract multiples of 22 until you get a number that is less
                 than 22)
        = 139 - (22 x 6)
        = 139 - 132
        = 7
    Step 3. Determine the Valid Alpha Code
        The remainder “7” corresponds to the Alpha Code letter “H” (see key
        dictionary). Therefore, the inventory number # 836 597 H in Figure 1 is
        valid.
    """

    # Define the valid input format regex
    format = re.compile("\d{6}[A-Z]{1}")

    # Check the input format to ensure that it follows the correct pattern, e.g.
    # NNNNNNA. If it doesn't, return False otherwise continue with validation
    # steps.
    if format.match(xn):
        # Define dictionary that contains key value pair to lookup the letter value
        # in the crossing number
        key = {
            0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
            9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
            17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
            25: 'Z',
        }

        # p = product,  m = multiplier
        p, m = 0, 1

        # Iterate through the first six digits and compute the total and remainder
        # based on the formula in steps 1 and 2.
        for i in xn[0:6]:
            p = (int(i) * m) + p
            m += 1
        r = p % 22

        # Use the dictionary key to get the corresponding alpha value and check
        # if ths input value matches the expected result.
        if xn == (xn[0:6] + key[r]):
            return True
        else:
            return False

    else:
        return False
