def main():
    s = input()
    o = s.count('o')
    x = s.count('x')
    q = s.count('?')
    if o > 4:
        print(0)
    elif o == 4:
        print(24)
    elif o == 3:
        print(36)
    elif o == 2:
        print(14 * 12 + 18)
    elif o == 1:
        print(4 * 12 + 4 * 11 + 4 * 10 + 4 * 9 + 4 * 8 + 4 * 7 + 4 * 6 + 4 * 5 + 4 * 4 + 4 * 3 + 4 * 2 + 4 * 1)
    elif o == 0:
        print(1 * 12 + 2 * 11 + 3 * 10 + 4 * 9 + 5 * 8 + 6 * 7 + 7 * 6 + 8 * 5 + 9 * 4 + 10 * 3 + 11 * 2 + 12 * 1)
