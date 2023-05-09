def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(0)
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

if __name__ == '__main__':
    main()