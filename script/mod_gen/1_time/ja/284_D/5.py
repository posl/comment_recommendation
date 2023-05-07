def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = 0
        q = 0
        for j in range(2, N):
            if N % j == 0:
                p = j
                N = N // j
                break
        for j in range(2, N):
            if N % j == 0:
                q = j
                N = N // j
                break
        print(p, q)

if __name__ == '__main__':
    main()