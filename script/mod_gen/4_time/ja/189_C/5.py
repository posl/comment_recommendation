def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            result = max(result, x * (j - i + 1))
    print(result)

if __name__ == '__main__':
    main()