def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, -1)
    ans = 0
    for i in range(1, n + 1):
        if p[i] == i - 1:
            ans += 1
            p[i] = p[i + 1]
    print(ans)
