def problem232_b():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    problem232_b()