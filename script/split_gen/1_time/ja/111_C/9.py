def main():
    n = int(input())
    v = list(map(int, input().split()))
    # v を /\/\/\/ にしたい
    # v を /\/\/\/ にするためには、
    # 1. v の要素をいくつか書き換える
    # 2. v の要素をいくつか削除する
    # 3. v の要素をいくつか追加する
    # ということをする必要がある。
    # 1. と 2. と 3. はいずれも、要素をいくつか選んで書き換えることになる。
    # 1. と 2. と 3. はどれも独立に考えることができるので、
    # これらを独立に考えたときの最小値を取ればよい。
    # 1. と 2. と 3. を独立に考える。
    # 1. と 2. と 3. のうち、最も要素を少なく書き換えることができるものを選ぶ。
    # 1. と 2. と 3. のうち、最も要素を少なく書き換えることができるものは、
    # 1. と 2. と 3. のうち、最も要素を多く書き換えることができるものと同じ。
    # 1. と 2. と 3. のうち、最も要素を多く書き換えることができるものは、
    # 1. と 2. と 3. のうち、最も要素を多く削除することができるものと同じ。
    # 1. と 2. と 3. の
