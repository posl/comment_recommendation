def ball(n,a,b):
    if a+b == 0:
        return 0
    elif a+b == 1:
        if a == 1:
            return 0
        else:
            return 1
    elif n <= a:
        return 0
    elif n <= a+b:
        return 1
    else:
        return ball(n-a-b,a,b)

if __name__ == '__main__':
    ball()