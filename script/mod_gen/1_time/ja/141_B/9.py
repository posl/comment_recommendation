def check(s):
    if len(s) == 0:
        return True
    if len(s) % 2 == 0:
        if s[0] not in ['L', 'U', 'D']:
            return False
        return check(s[1:])
    else:
        if s[0] not in ['R', 'U', 'D']:
            return False
        return check(s[1:])
S = input()
print('Yes' if check(S) else 'No')

if __name__ == '__main__':
    check()