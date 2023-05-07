def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for s in S:
        a = (s - 3) // 3
        b = (s - 3) // 4
        if a <= 0 or b <= 0:
            ans += 1
            continue
        if 4 * a * b + 3 * a + 3 * b != s:
            ans += 1
    print(ans)
