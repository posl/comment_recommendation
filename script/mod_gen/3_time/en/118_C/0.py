def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = A[-1]
    for i in range(N-2, -1, -1):
        ans = (A[i] + ans - 1) // A[i] * A[i]
    print(ans)

if __name__ == '__main__':
    main()