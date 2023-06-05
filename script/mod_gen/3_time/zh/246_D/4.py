def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    for a in range(1, 1000000):
        if n < a**3:
            break
        for b in range(a, 1000000):
            if n < a**3 + a**2*b:
                break
            if n == a**3 + a**2*b + a*b**2 + b**3:
                print(a**3 + a**2*b + a*b**2 + b**3)
                return

if __name__ == '__main__':
    main()