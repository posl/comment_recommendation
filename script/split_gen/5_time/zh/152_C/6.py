def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if p[i] <= p[i-1]:
            ans += 1
    print(ans)
