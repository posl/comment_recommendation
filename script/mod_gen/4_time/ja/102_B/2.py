def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if ans < abs(A[i] - A[j]):
                ans = abs(A[i] - A[j])
    print(ans)

if __name__ == '__main__':
    main()