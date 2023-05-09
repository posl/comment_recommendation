def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        p = 0
        q = 0
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                p = i
                q = N // i
                break
        print(p, q)

if __name__ == '__main__':
    main()