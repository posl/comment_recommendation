def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        for a in A:
            if a <= k:
                k += 1
        print(k)

if __name__ == '__main__':
    main()