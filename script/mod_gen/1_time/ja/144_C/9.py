def solve(n):
    # 1 から n までの和を求める
    def sum(n):
        return (1 + n) * n // 2
    # n が書かれているマスに到達するまでに必要な移動回数の最小値を求める
    def count(n):
        if n == 1:
            return 0
        # n が書かれているマスに到達するまでに必要な移動回数の最小値
        count = 0
        # 1 から n までの和
        s = 0
        # 1 から n までの和が n 未満になるまで繰り返す
        while s < n:
            # 1 から n までの和を n で割った商を求める
            # 1 から n までの和が n 未満になるまで繰り返す
            while s < n:
                # 1 から n までの和を n で割った商を求める
                s = sum(n // (count + 1))
                # 1 から n までの和が n 未満になるまで繰り返す
                if s < n:
                    # 1 から n までの和を n で割った商を求める
                    count += 1
        return count
    # n が書かれているマスに到達するまでに必要な移動回数の最小値を求める
    return count(n)

if __name__ == '__main__':
    solve()