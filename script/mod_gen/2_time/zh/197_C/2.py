def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = x | A[j]
            y = x
            for k in range(j+1, N):
                y = y ^ A[k]
                ans = max(ans, y)
    print(ans)

if __name__ == '__main__':
    main()