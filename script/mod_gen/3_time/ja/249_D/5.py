def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] * A[k] == A[j] * A[j]:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()