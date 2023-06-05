def func(a):
    #print(a)
    if len(a) == 1:
        if a[0] % 2 == 0:
            return 1
        else:
            return 0
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        if sum % len(a) == 0:
            return 1
        else:
            return 0

if __name__ == '__main__':
    func()