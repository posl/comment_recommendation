def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    ans = 0
    for i in range(n):
        if h[i] < h[i + 1]:
            ans = h[i + 1]
    print(ans)
