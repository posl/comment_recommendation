def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    cnt = 1
    x = X - 1
    while A[x] != X - 1:
        x = A[x]
        cnt += 1
        if cnt > N:
            print(-1)
            return
    print(cnt)

if __name__ == '__main__':
    main()