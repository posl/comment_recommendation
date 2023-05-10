def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    ans = t[-1]
    for i in range(n-2, -1, -1):
        ans = min(ans, t[i] + t[-1-i])
    print(ans)
