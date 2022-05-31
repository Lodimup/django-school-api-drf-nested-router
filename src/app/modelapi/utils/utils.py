import uuid

def gen_uuid(length: int=20) -> str:
    """
    Generate a random UUID string.
    :param length: length of the UUID string
    :return: UUID string
	Chance of collision is 1 in 34^20, low enough for our purposes
	Be mindful if length < 20
    """
    return uuid.uuid4().hex[:length].upper()


def sanitize_name(name: str) -> str:
    """
    Sanitize a name string.
    :param name: name string
    :return: sanitized name string
    """
    return name.strip().capitalize()


def name_isvalid(name: str) -> bool:
    """
    Check if a name string is valid.
    :param name: name string
    :return: True if valid, False otherwise
    """
    return len(name) > 0 and name.isalpha()


def school_name_isvalid(name: str) -> bool:
    """
    Check if a school name string is valid.
    :param name: school name string
    :return: True if valid, False otherwise
    """
    l_valid_chars = [' ', '-', ',',]
    for char in l_valid_chars:
        name = name.replace(char, '')

    return len(name) > 0 and name.isalpha()
