def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] % 2 == 0:
            ans += 1
        elif s[i] % 3 == 0:
            ans += 1
        elif s[i] % 5 == 0:
            ans += 1
    print(ans)
