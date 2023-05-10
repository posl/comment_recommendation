def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i + 1 == p[p[i] - 1]:
            ans += 1
    print(ans)
