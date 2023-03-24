def convert_to_numbers(numeral, d):
    """converts a Roman numeral into a decimal number"""
    count = 0
    total = 0
    gen = generate_symbol(numeral)
    curr = next(gen)
    while count < len(numeral):

        prev, curr = curr, next(gen)
        if d[curr] > d[prev]:
            total += d[curr] - d[prev]
            prev, curr = curr, next(gen)
            count += 2
        else:
            total += d[prev]
            count += 1

    return total


def generate_symbol(numeral):
    """generates the next symbol of the Roman Numeral"""
    for let in numeral:
        yield let
    while True:
        yield 'Zero'


def convert_to_numerals(num, d):
    """takes a number and converts it into Roman Numerals, without subtractive notation"""
    numeral = ''
    while num > 0:
        index = index_finder(num, d)
        num -= list(d.values())[index]
        numeral += list(d.keys())[index]
    return numeral


def index_finder(num, d):
    """Finds the index of the largest Roman Numeral less than or equal to the number"""
    for i, val in enumerate(d.values()):
        if val > num:
            return i-1
    return -1


def convert_to_numerals2(num, d):
    """uncompleted implementation of convert to numerals including subtraction notation"""
    count = 0
    numeral = ''
    gen = num_generator(num)
    curr = next(gen)
    while num > 0:

        curr = next(gen)
        index = index_finder(num, d)
        if curr == 4:
            numeral += list(d.keys())[index - 1]
            numeral += list(d.keys())[index]

        elif curr == 9:
            numeral += list(d.keys())[index - 2]
            numeral += list(d.keys())[index]

        else:
            while curr > 0:
                num -= list(d.values())[index]
                numeral += list(d.keys())[index]
                curr -= 1

        count += 1

    return numeral


def num_generator(num):
    """generator that iterates through the number"""
    for digit in str(num):
        yield int(digit)
    while True:
        yield None


d = {
    'Zero': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
response = input('What Roman Numeral would you like to convert? ')
num = convert_to_numbers(response, d)
print(num)
numerals = convert_to_numerals(num, d)
print(numerals)
