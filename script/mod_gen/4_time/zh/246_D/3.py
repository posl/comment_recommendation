def main():
    N = int(input())
    a = 1
    b = 1
    while True:
        if N <= a**3 + a**2*b + a*b**2 + b**3:
            break
        else:
            a += 1
            b = a
    print(a**3 + a**2*b + a*b**2 + b**3)

if __name__ == '__main__':
    main()