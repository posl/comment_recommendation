def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        kth = 0
        for i in range(N):
            if A[i] == x:
                kth += 1
            if kth == k:
                print(i+1)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()