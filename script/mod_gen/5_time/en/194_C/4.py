def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1])**2
    print(ans)
    return

if __name__ == '__main__':
    main()