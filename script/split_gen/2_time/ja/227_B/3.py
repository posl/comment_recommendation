def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        a = (s[i] - 3) // 3
        b = (s[i] - 3) // 4
        if a > 0 and b > 0:
            if (4 * a * b + 3 * a + 3 * b) == s[i]:
                cnt += 1
    print(n - cnt)
