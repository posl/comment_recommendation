def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        tmp = 0
        for j in range(N):
            if A[j] == x:
                k -= 1
            if k == 0:
                tmp = j
                break
        if tmp:
            print(tmp+1)
        else:
            print(-1)

if __name__ == '__main__':
    main()