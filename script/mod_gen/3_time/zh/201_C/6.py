def count_passwords(s, x):
    if len(s) == 0:
        return 1
    elif s[0] == '?':
        return count_passwords('o' + s[1:], x) + count_passwords('x' + s[1:], x)
    elif s[0] == 'o':
        return count_passwords('o' + s[1:], x)
    elif s[0] == 'x':
        return count_passwords('x' + s[1:], x)
    else:
        return count_passwords(s[1:], x)
s = input()
x = input()
print(count_passwords(s, x))
