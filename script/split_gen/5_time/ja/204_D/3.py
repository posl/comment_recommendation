def main():
    n = int(input())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = max(ans, t[i])
    print(ans)
