def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    A = sorted(A)
    cnt = 0
    prev = A[0]
    for i in range(1, N):
        if prev == A[i]:
            cnt += 1
            prev = -1
        else:
            prev = A[i]
    print(cnt)

if __name__ == '__main__':
    main()