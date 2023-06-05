def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = 0
    j = 0
    cnt = 0
    while i < n:
        if a[i] > b[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
    print(cnt)

if __name__ == '__main__':
    solve()