def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    for a in range(100):
        for b in range(100):
            if N <= a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3:
                print(a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3)
                return

if __name__ == '__main__':
    main()