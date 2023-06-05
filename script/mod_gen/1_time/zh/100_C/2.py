def problem100_c():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        tmp = a[i]
        while tmp % 2 == 0:
            tmp //= 2
            ans += 1
    print(ans)

if __name__ == '__main__':
    problem100_c()