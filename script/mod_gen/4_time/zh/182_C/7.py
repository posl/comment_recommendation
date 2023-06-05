def check(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 3 == 0:
        return True
    else:
        return False
n = int(input())

if __name__ == '__main__':
    check()