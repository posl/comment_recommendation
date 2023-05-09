def solve():
    # === 数値の入力 ===
    # N = int(input())
    # a, b = map(int, input().split())
    # A = list(map(int, input().split()))
    S = input()
    # ==================
    ans = 0
    cnt = 0
    for s in S:
        if s == "R":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    solve()