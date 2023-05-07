def main():
    N = int(input())
    for i in range(N, 10**18):
        for a in range(0, 1000):
            for b in range(0, 1000):
                if i == a**3 + a**2*b + a*b**2 + b**3:
                    print(i)
                    return

if __name__ == '__main__':
    main()