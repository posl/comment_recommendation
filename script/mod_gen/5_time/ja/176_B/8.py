def check(n):
    s = str(n)
    l = len(s)
    sum = 0
    for i in range(l):
        sum += int(s[i])
    if sum % 9 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    check()