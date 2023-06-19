def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if s[i] == '1' and s[i-1] == '0':
            ans += 1
    if s[-1] == '0':
        ans += 1
    print(ans)
