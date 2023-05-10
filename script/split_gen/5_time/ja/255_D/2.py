def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    a.append(0)
    a.append(0)
    x.sort()
    x.append(0)
    x.append(0)
    ans = 0
    for i in range(q):
        ans += abs(a[i] - a[i+1]) * (i + 1)
    print(ans)
