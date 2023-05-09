def solve():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    # まずCをソートする
    C.sort()
    # Cの値が同じものがいくつあるかを数える
    count = 1
    tmp = C[0]
    C_count = []
    for i in range(1, N):
        if tmp == C[i]:
            count += 1
        else:
            C_count.append(count)
            count = 1
            tmp = C[i]
    C_count.append(count)
    # C_countの累積和をとる
    C_count = [0] + C_count
    for i in range(1, len(C_count)):
        C_count[i] += C_count[i-1]
    # C_countの累積和を使って解を求める
    ans = 1
    for i in range(len(C_count)-1):
        ans *= C_count[i+1] - C_count[i] + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()