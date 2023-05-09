def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    if A[0] != 0:
        print(-1)
        return
    cnt = 0
    for i in range(N - 1):
        if A[i] >= A[i + 1]:
            cnt += A[i] - A[i + 1]
        else:
            if A[i + 1] - A[i] > 1:
                print(-1)
                return
    print(cnt)

if __name__ == '__main__':
    main()