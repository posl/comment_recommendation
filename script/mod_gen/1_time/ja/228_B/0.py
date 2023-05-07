def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if X == A[X-1]:
            cnt += 1
            break
        else:
            X = A[X-1]
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()