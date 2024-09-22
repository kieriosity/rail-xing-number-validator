import re

# Constants for configuration
MODULO_BASE = 22
KEY_MAPPING = "ABCDEFGHIJLMNPRSTUVWXY"
XING_FORMAT_REGEX = re.compile(r'^\d{6}[A-Z]$')

def crossing_number_validation(xing_number: str) -> bool:
    """
    Validates a crossing number consisting of six digits followed by an uppercase letter.
    The letter is determined by a checksum algorithm.

    Args:
        xing_number (str): The crossing number to validate.

    Returns:
        bool: True if the crossing number is valid, False otherwise.
    """
    # Normalize input by stripping whitespace and converting to uppercase
    xing_number = xing_number.strip().upper()

    # Validate the format using the precompiled regex
    if not XING_FORMAT_REGEX.match(xing_number):
        return False

    # Calculate the checksum
    try:
        total = sum(int(d) * i for i, d in enumerate(xing_number[:6], 1))
    except ValueError:
        # Safeguard against non-digit characters, though regex should prevent this
        return False

    # Determine the expected letter based on the checksum
    remainder = total % MODULO_BASE
    expected_letter = KEY_MAPPING[remainder]

    # Validate the checksum letter
    return xing_number[-1] == expected_letter
