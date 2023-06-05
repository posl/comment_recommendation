def main():
    n, k = map(int, input().split())
    s = input()
    # 0,1の状態を数える
    cnt = [0]
    for i in range(n):
        cnt.append(cnt[-1] + int(s[i]))
    # 01の状態を数える
    cnt2 = [0]
    for i in range(n):
        cnt2.append(cnt2[-1] + 1 if s[i] == '0' else cnt2[-1])
    # 01の状態から、K回の操作で得られる01の状態の最大値を求める
    ans = 0
    for i in range(n):
        l = 0
        r = min(n, i + k * 2 + 1)
        while r - l > 1:
            m = (l + r) // 2
            if cnt2[m] - cnt2[i] <= k:
                l = m
            else:
                r = m
        ans = max(ans, cnt[l] - cnt[i])
    print(ans)
