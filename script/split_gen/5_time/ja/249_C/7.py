def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # Sを2進数で表したときのビットが立っているところが登場する文字列として選ばれたものになる
    # 例えばS[0] = "abc"のとき、S[0]を選んだときのビットは00000000000000000000000001となる
    # S[0], S[1], S[2]を選んだときのビットは00000000000000000000000011となる
    # S[0], S[1], S[2], S[3]を選んだときのビットは00000000000000000000000011となる
    # このように、ビットを立てるところを全探索する
    # このとき、ビットが立っているところの文字を集めて、
    # それぞれの文字の出現数を集計して、Kと一致するものを数える
    ans = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(S[j])
        if len(tmp) == 0:
            continue
        cnt = [0] * 26
        for s in tmp:
            for c in s:
                cnt[ord(c) - ord('a')] += 1
        if max(cnt) <= K:
            ans = max(ans, sum(cnt))
    print(ans)
