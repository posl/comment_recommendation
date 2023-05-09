def problems200_c():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 200 for i in a]
    a.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            ans += (cnt * (cnt - 1)) // 2
            cnt = 1
    ans += (cnt * (cnt - 1)) // 2
    print(ans)

if __name__ == '__main__':
    problems200_c()