def main():
    N = int(input())
    p = 0
    q = 0
    for i in range(2, N + 1):
        if N % i == 0:
            p = i
            break
    q = N // p
    print(p, q)

if __name__ == '__main__':
    main()