def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if all(h[i] >= h[j] for j in range(i)):
                ans += 1
    print(ans)
