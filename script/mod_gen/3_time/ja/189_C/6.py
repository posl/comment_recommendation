def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_orange = 0
    for i in range(N):
        for j in range(i, N):
            x = 10**9
            for k in range(i, j+1):
                x = min(x, A[k])
            max_orange = max(max_orange, x*(j-i+1))
    print(max_orange)

if __name__ == '__main__':
    main()