def main():
    K = int(input())
    if K <= 200:
        print(K)
        return
    K -= 200
    L = 3
    while True:
        if K < 2 ** (L - 2):
            break
        K -= 2 ** (L - 2)
        L += 1
    S = 2 ** (L - 2)
    K += 1
    N = 0
    for i in range(L - 1):
        if K & (1 << i):
            N = N * 10 + 2
        else:
            N = N * 10
    print(N)

if __name__ == '__main__':
    main()