def problems226_b():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            for j in range(i):
                if a[i] == a[j]:
                    break
                if j == i - 1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    problems226_b()