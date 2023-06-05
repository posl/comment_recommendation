def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    ans = 0
    for i in range(1, N+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            ans += 1
        elif h[i-1] > h[i] and h[i] < h[i+1]:
            ans += 1
    print(ans)
