def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * N
    for i in range(N):
        if a[i] - i - 1 >= 0:
            b[a[i] - i - 1] += 1
    ans = 0
    for i in range(N):
        if a[i] + i + 1 <= N:
            ans += b[a[i] + i]
    print(ans)

if __name__ == '__main__':
    main()