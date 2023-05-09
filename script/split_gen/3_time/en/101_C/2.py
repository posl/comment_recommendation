def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(0, n, k):
        ans += 1
    print(ans)
