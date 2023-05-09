def solve(input_string):
    if input_string[0] != 'A':
        return 'WA'
    if input_string[2:-1].count('C') != 1:
        return 'WA'
    if input_string[1] == 'C' or input_string[-1] == 'C':
        return 'WA'
    if input_string[1].isupper() or input_string[-1].isupper():
        return 'WA'
    return 'AC'
