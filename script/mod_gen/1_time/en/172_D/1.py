def main():
    N = int(input())
    f = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            f[j] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += i * f[i]
    print(ans)

if __name__ == '__main__':
    main()