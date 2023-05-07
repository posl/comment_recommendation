def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    cnt = 1
    next = X
    while True:
        if A[next] == X:
            break
        next = A[next]
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()