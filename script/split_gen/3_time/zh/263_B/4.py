def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = i + 1
        while x != -1:
            x = p[x - 1]
            ans += 1
        print(ans)
        ans = 0
