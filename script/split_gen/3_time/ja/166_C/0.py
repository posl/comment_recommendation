def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if a[j] == i + 1 and h[i] <= h[b[j] - 1]:
                flag = False
                break
            if b[j] == i + 1 and h[i] <= h[a[j] - 1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
