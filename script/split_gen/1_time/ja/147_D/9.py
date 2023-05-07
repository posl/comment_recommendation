def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    # 2進数へ
    bin_list = []
    for a in A:
        bin_list.append(bin(a)[2:])
    # 2進数の桁数を揃える
    max_len = max([len(a) for a in bin_list])
    bin_list = [a.zfill(max_len) for a in bin_list]
    # 1の数を数える
    cnt = [0] * max_len
    for a in bin_list:
        for i, b in enumerate(a[::-1]):
            if b == "1":
                cnt[i] += 1
    # 答えを求める
    ans = 0
    for i, c in enumerate(cnt):
        ans += (2 ** i) * c * (N - c)
        ans %= MOD
    print(ans)
