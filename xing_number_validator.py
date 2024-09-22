import re

def crossing_number_validation(xing_number):
    """
    Validates a crossing number based on specific rules.

    A valid crossing number consists of six digits followed by an uppercase letter.
    The letter is determined by a checksum algorithm.

    Steps to Validate:
    1. Compute the Total Numeric Value:
        Sum of each digit multiplied by its position (1-based).
    2. Find Remainder when divided by 22.
    3. Map the remainder to the corresponding uppercase letter.
    4. The letter in the input must match the mapped letter.

    Example:
        Input: 836597H
        Calculation:
            (8*1) + (3*2) + (6*3) + (5*4) + (9*5) + (7*6) = 139
            139 % 22 = 7
            Corresponding Letter: 'H'
        Result: Valid
    """
    
    # Define the valid input format regex
    xing_format = re.compile(r"^\d{6}[A-Z]$")

    # Convert input to uppercase to ensure consistency
    xing_number = xing_number.upper()

    # Check the input format to ensure that it follows the correct pattern
    if not xing_format.match(xing_number):
        return False

    # Define the key string for mapping remainders to letters
    key = "ABCDEFGHIJKLMNOPQRSTUV"

    # Compute the total using a generator expression with enumerate
    total = sum(int(digit) * (index + 1) for index, digit in enumerate(xing_number[:6]))
    
    # Calculate the remainder
    remainder = total % 22

    # Ensure the remainder is within the key's range
    if remainder >= len(key):
        return False  # This should not happen if key length matches modulo base

    # Get the expected letter from the key
    expected_letter = key[remainder]

    # Validate the letter
    return xing_number[-1] == expected_letter

