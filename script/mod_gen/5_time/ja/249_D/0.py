def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] * A[j] in A:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()