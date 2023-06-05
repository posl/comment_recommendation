def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for l in range(N):
        for r in range(l, N):
            x = min(A[l:r+1])
            if max < x * (r-l+1):
                max = x * (r-l+1)
    print(max)

if __name__ == '__main__':
    main()