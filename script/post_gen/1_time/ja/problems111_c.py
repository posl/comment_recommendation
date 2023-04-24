Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    c1_max = c1.most_common(1)[0]
    c2_max = c2.most_common(1)[0]
    if c1_max[0] != c2_max[0]:
        print(n - c1_max[1] - c2_max[1])
    else:
        # 1種類の数が最大値になる場合
        if len(c1) == 1 and len(c2) == 1:
            print(n // 2)
        # 2種類の数が最大値になる場合
        else:
            c1_max2 = c1.most_common(2)[1]
            c2_max2 = c2.most_common(2)[1]
            print(n - max(c1_max[1] + c2_max2[1], c1_max2[1] + c2_max[1]))

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    d1 = {}
    d2 = {}
    for i in v1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    for i in v2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
    d1 = sorted(d1.items(), key=lambda x: -x[1])
    d2 = sorted(d2.items(), key=lambda x: -x[1])
    if d1[0][0] == d2[0][0]:
        if len(d1) == 1 and len(d2) == 1:
            print(n//2)
        elif len(d1) == 1:
            print(n//2 - d2[1][1])
        elif len(d2) == 1:
            print(n//2 - d1[1][1])
        else:
            print(min(n - d1[0][1] - d2[1][1], n - d1[1][1] - d2[0][1]))
    else:
        print(n - d1[0][1] - d2[0][1])

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = [0] * (10**5 + 1)
    b = [0] * (10**5 + 1)
    for i in range(n):
        if i % 2 == 0:
            a[v[i]] += 1
        else:
            b[v[i]] += 1
    a_max = max(a)
    b_max = max(b)
    a_max_i = a.index(a_max)
    b_max_i = b.index(b_max)
    if a_max_i != b_max_i:
        print(n - a_max - b_max)
    else:
        a.sort(reverse=True)
        b.sort(reverse=True)
        print(n - max(a[0] + b[1], a[1] + b[0]))

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    if n == 2:
        print(0)
        return
    a = v[0::2]
    b = v[1::2]
    a.sort()
    b.sort()
    c = a[0]
    d = b[0]
    e = a[-1]
    f = b[-1]
    if c == e and d == f:
        print(n - max(a.count(c), b.count(d)))
    elif c == e:
        print(n - a.count(c))
    elif d == f:
        print(n - b.count(d))
    else:
        print(n - a.count(c) - b.count(d))

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int,input().split()))
    cnt = [0]*(10**5+1)
    for i in range(n):
        cnt[v[i]] += 1
    cnt.sort(reverse=True)
    ans = 0
    ans += cnt[0]
    ans += cnt[1]
    ans = n-ans
    print(ans)

=======
Suggestion 6

def main():
    # 入力
    n = int(input())
    v = list(map(int, input().split()))
    # 偶数番目と奇数番目に分ける
    v_odd = v[0::2]
    v_even = v[1::2]
    # それぞれの数の個数をカウント
    from collections import Counter
    c_odd = Counter(v_odd)
    c_even = Counter(v_even)
    # それぞれの最も多い数を求める
    max_odd = c_odd.most_common()[0][0]
    max_even = c_even.most_common()[0][0]
    # 最も多い数が同じ場合
    if max_odd == max_even:
        # それぞれの最も多い数以外の数の個数を求める
        max_odd_count = c_odd.most_common()[0][1]
        max_even_count = c_even.most_common()[0][1]
        max_odd_count2 = c_odd.most_common()[1][1]
        max_even_count2 = c_even.most_common()[1][1]
        # それぞれの最も多い数以外の数の個数の和が答え
        print(n - max_odd_count - max_even_count2)
    # 最も多い数が異なる場合
    else:
        # それぞれの最も多い数の個数を求める
        max_odd_count = c_odd.most_common()[0][1]
        max_even_count = c_even.most_common()[0][1]
        # それぞれの最も多い数の個数の和が答え
        print(n - max_odd_count - max_even_count)

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_odd = v[::2]
    v_even = v[1::2]
    v_odd_count = max(v_odd.count(x) for x in set(v_odd))
    v_even_count = max(v_even.count(x) for x in set(v_even))
    ans = min(n - v_odd_count, n - v_even_count)
    if len(set(v_odd)) == len(set(v_even)) == 1 and v_odd[0] != v_even[0]:
        ans = min(ans, n // 2)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))

    # 1の個数と2の個数を数える
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if i % 2 == 0:
            if v[i] == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if v[i] == 1:
                cnt2 += 1
            else:
                cnt1 += 1

    # 1の個数と2の個数のうち少ない方の数を書き換える
    if cnt1 < cnt2:
        print(cnt1)
    else:
        print(cnt2)

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    # 1種類の数字があるか
    if len(set(v)) == 1:
        print(n // 2)
        return
    # 2種類の数字がある場合
    # 1種類の数字の数をカウント
    count = 0
    for i in range(n):
        if v[i] == v[0]:
            count += 1
        else:
            break
    # 1種類の数字を前後に並べる
    v1 = v[:count]
    v2 = v[count:]
    v = v1 + v2
    # 1種類の数字の数が偶数か奇数か
    if count % 2 == 0:
        # 偶数の場合
        ans = min(count // 2 + (n - count) // 2, (count + 1) // 2 + (n - count - 1) // 2)
    else:
        # 奇数の場合
        ans = min((count + 1) // 2 + (n - count - 1) // 2, (count - 1) // 2 + (n - count + 1) // 2)
    print(ans)

=======
Suggestion 10

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
