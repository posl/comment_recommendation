def main():
    N = int(input())
    N = N + 1
    n = 0
    for i in range(1, N):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            n = n + 1
    print(n)

if __name__ == '__main__':
    main()