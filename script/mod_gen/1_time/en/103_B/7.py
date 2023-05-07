def check_rotation(s, t):
    if s == t:
        return 'Yes'
    else:
        for i in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                return 'Yes'
    return 'No'
s = input()
t = input()
print(check_rotation(s, t))

if __name__ == '__main__':
    check_rotation()