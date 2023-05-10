def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    max = 0
    for i in range(n):
        if h[i] >= max:
            ans += 1
            max = h[i]
    print(ans)
