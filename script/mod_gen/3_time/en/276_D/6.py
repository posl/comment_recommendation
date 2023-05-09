def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == A[N-1]:
        print(0)
        return
    cnt = 0
    while True:
        cnt += 1
        A[0] *= 2
        A.sort()
        if A[0] == A[N-1]:
            print(cnt)
            return
        if A[0] > A[N-1]:
            print(-1)
            return

if __name__ == '__main__':
    main()