def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N + 1):
        if i == A[A[i - 1] - 1]:
            ans += 1
    print(ans // 2)

if __name__ == '__main__':
    main()