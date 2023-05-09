def func(n, s):
    count = 0
    for i in range(n):
        a = 1
        while True:
            b = (s[i]-3*a)//(4*a+3)
            if s[i] == 4*a*b+3*a+3*b and b > 0:
                break
            a += 1
            if a > s[i]:
                count += 1
                break
    return count

if __name__ == '__main__':
    func()