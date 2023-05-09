def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if x >= sum(l[:i+1]):
            ans += 1
    print(ans)
