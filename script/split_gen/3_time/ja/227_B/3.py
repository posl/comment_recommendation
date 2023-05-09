def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = (s[i] - 3) // 3
        b = (s[i] - 3) // 4
        if a <= 0 or b <= 0:
            continue
        if 4 * a * b + 3 * a + 3 * b == s[i]:
            continue
        else:
            ans += 1
    print(ans)
