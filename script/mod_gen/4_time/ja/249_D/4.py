def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i] == A[j]:
                continue
            if A[i] % A[j] != 0:
                continue
            if A[i] // A[j] in A:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()