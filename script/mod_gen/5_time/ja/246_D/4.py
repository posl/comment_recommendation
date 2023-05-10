def main():
    n = int(input())
    #n = 999999999989449206
    #n = 9
    x = n
    while True:
        a = 0
        b = 0
        while True:
            if x < (a**3 + a**2*b + a*b**2 + b**3):
                break
            if x == (a**3 + a**2*b + a*b**2 + b**3):
                print(x)
                return
            a += 1
            b += 1
        x += 1

if __name__ == '__main__':
    main()