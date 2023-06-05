def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    ans = 0
    for i in range(1, n + 1):
        if h[i - 1] < h[i]:
            ans += h[i] - h[i - 1]
        if h[i + 1] < h[i]:
            ans += h[i] - h[i + 1]
    print(ans)
