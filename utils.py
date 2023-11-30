### Utils Functions

import re

def isCNPJ(cnpj: str):
    """Function to verify if a Brazilian CNPJ is valid

    Dependences:
        re: Library of regular expression

    Args:
        cnpj (str): The CNPJ to validate.

    Returns:
        bool: True if the CNPJ is valid, False otherwise.
    """

    # Remove any non-numeric characters.
    cnpj = re.sub(r'\D', '', cnpj)

    # Check if the length of the CNPJ is not equal to 14.
    if len(cnpj) != 14:
        return False

    # Verify if informed CNPJ is one of invalids list
    invalid_list = [
        '00000000000000',
        '11111111111111',
        '22222222222222',
        '33333333333333',
        '44444444444444',
        '55555555555555',
        '66666666666666',
        '77777777777777',
        '88888888888888',
        '99999999999999'
    ]
    if cnpj in invalid_list:
        return False

    # Extract the verification digits.
    verification_digits = cnpj[-2:]

    # Calculate the first verification digit.
    cnpj = cnpj[:-2]
    weights = [6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    cnpj_sum = sum(int(digit) * weight for digit, weight in zip(cnpj, weights))
    digit1 = cnpj_sum % 11
    digit1 = 0 if digit1 > 9 else digit1

    # Check if the calculated first verification digit matches the first verification digit.
    if digit1 != int(verification_digits[0]):
        return False

    # Calculate the second verification digit.
    cnpj += str(digit1)
    weights = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    cnpj_sum = sum(int(digit) * weight for digit, weight in zip(cnpj, weights))
    digit2 = cnpj_sum % 11
    digit2 = 0 if digit2 > 9 else digit2

    # Check if the calculated second verification digit matches the second verification digit.
    if digit2 != int(verification_digits[1]):
        return False

    # The CNPJ is valid.
    return True

def isCPF(cpf: str):
    """Function to verify if a Brazilian CPF is valid

    Dependences:
        re: Library of regular expression

    Args:
        cpf (str): The CPF to validate.

    Returns:
        bool: True if the CPF is valid, False otherwise.
    """

    # Remove any non-numeric characters.
    cpf = re.sub(r'\D', '', cpf)

    # Check if the length of the CNPJ is not equal to 11.
    if len(cpf) != 11:
        return False

    # Verify if informed CPF is one of invalids list
    invalid_list = [
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999'
    ]
    if cpf in invalid_list:
        return False

    # Extract the verification digits.
    verification_digits = cpf[-2:]

    # Calculate the first verification digit.
    cpf = cpf[:-2]
    cpf_sum = sum(int(digito) * (index + 1) for index, digito in enumerate(cpf))
    digit1 = cpf_sum % 11
    digit1 = 0 if digit1 > 9 else digit1
    
    # Check if the calculated first verification digit matches the first verification digit.
    if digit1 != int(verification_digits[0]):
        return False

    # Calculate the second verification digit.
    cpf += str(digit1)
    cpf_sum = sum(int(digito) * index for index, digito in enumerate(cpf))
    digit2 = cpf_sum % 11
    digit2 = 0 if digit2 > 9 else digit2

    # Check if the calculated second verification digit matches the second verification digit.
    if digit2 != int(verification_digits[1]):
        return False

    # The CPF is valid.
    return True