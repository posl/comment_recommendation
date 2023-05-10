def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
    ans = ans - min(a)
    print(ans)
