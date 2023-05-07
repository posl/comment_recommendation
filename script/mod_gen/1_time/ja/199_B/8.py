def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = ans + (B[i] - A[i] + 1)
    print(ans)

if __name__ == '__main__':
    main()