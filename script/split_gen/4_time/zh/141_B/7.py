def check(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == 'L':
            return False
        elif i % 2 == 1 and s[i] == 'R':
            return False
    return True
s = input()
