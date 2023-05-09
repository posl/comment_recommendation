def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n//2):
        if a[i] != a[-1-i]:
            ans += 1
    print(ans)
