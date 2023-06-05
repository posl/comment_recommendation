def problems148_d():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    if b[0] != 1:
        print(-1)
        return
    for i in range(1, n):
        if b[i] == 0:
            print(-1)
            return
    ans = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    problems148_d()