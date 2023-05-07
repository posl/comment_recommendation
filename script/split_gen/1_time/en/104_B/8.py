def solve(string):
    if string[0] != 'A':
        return 'WA'
    if string[2:-1].count('C') != 1:
        return 'WA'
    for s in string:
        if s != 'A' and s != 'C' and s.isupper():
            return 'WA'
    return 'AC'
