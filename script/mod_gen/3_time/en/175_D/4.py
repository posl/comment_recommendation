def main():
    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        # i番目のマスからスタートする
        # そのマスに到達するまでのループの長さを求める
        loop_len = 0
        j = i
        while True:
            j = p[j]
            loop_len += 1
            if j == i:
                break
        # ループの長さがk以下なら、ループの全ての要素を通る
        # ループの長さがkより大きければ、ループの長さがkになるまでの要素を通る
        # それぞれの場合で、最大の値を求める
        if loop_len <= k:
            loop_max = 0
            for j in range(loop_len):
                loop_max += c[p[i + j]]
                ans = max(ans, loop_max + (k - loop_len) // loop_len * max(0, loop_max))
        else:
            loop_max = 0
            for j in range(k):
                loop_max += c[p[i + j]]
                ans = max(ans, loop_max)
    print(ans)

if __name__ == '__main__':
    main()