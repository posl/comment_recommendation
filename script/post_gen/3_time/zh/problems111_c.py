Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = 0
    c2 = 0
    for i in range(1, n // 2 + 1):
        if v1.count(i) > v1.count(i + 1):
            c1 += v1.count(i + 1)
            c2 += v2.count(i)
        else:
            c1 += v1.count(i)
            c2 += v2.count(i + 1)
    print(n - max(c1, c2) * 2)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0 and a[i] == a[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    v = list(map(int,input().split()))
    a = [0]*100001
    b = [0]*100001
    for i in range(n):
        if i % 2 == 0:
            a[v[i]] += 1
        else:
            b[v[i]] += 1
    a_max = max(a)
    b_max = max(b)
    if a_max == b_max:
        if a_max == n//2:
            print(n//2)
        else:
            print(n//2)
    else:
        print(n-a_max-b_max)

=======
Suggestion 4

def solve(n, v):
    v0 = v[::2]
    v1 = v[1::2]
    c0 = max(v0, key=v0.count)
    c1 = max(v1, key=v1.count)
    if c0 == c1:
        return min(v0.count(c0) + v1.count(c1), v0.count(c0) + v1.count(c1))
    else:
        return len(v0) - max(v0.count(c0), v1.count(c1))

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1).most_common()
    c2 = Counter(v2).most_common()
    ans = 0
    if c1[0][0] == c2[0][0]:
        if len(c1) == 1 and len(c2) == 1:
            ans = n // 2
        elif len(c1) == 1:
            ans = n // 2 - c2[1][1]
        elif len(c2) == 1:
            ans = n // 2 - c1[1][1]
        else:
            ans = n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1])
    else:
        ans = n - c1[0][1] - c2[0][1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 1. 2つの異なる数字があるかどうかを確認する
    # 2. 2つの異なる数字がある場合は、/\/\/\/の条件を満たすために置き換える必要がある
    # 2.1. 置換する場合は、2つの異なる数字のうち、少ない方の出現回数を数える
    # 2.2. 置換しない場合は、2つの異なる数字のうち、多い方の出現回数を数える
    # 3. 2.1と2.2のうち、小さい方が答え

    # 1
    if len(set(a)) == 1:
        print(n // 2)
        return

    # 2
    count = [0] * 100001
    for i in range(n):
        count[a[i]] += 1

    # 2.1
    count1 = 0
    for i in range(100001):
        if count[i] > 0:
            count1 += 1

    # 2.2
    count2 = 0
    for i in range(100001):
        count2 = max(count2, count[i])

    # 3
    print(min(count1, count2))

=======
Suggestion 7

def get_min_replaced_num(n, v):
    # 从左到右找到第一个不同的数
    for i in range(n):
        if v[i] != v[0]:
            break
    # 从右到左找到第一个不同的数
    for j in range(n-1, -1, -1):
        if v[j] != v[-1]:
            break
    # 如果i和j相遇，说明整个数组都是相同的数
    if i == j:
        return n // 2
    # 如果i和j相邻，说明只有两个数，且相邻的两个数相等
    if i + 1 == j:
        return n // 2
    # 如果i和j不相邻，说明有两个数，且不相等
    return n - j + i

=======
Suggestion 8

def solve():
    n = int(input())
    v = [int(_) for _ in input().split()]
    even = v[::2]
    odd = v[1::2]
    even_count = {}
    odd_count = {}
    for e in even:
        if e in even_count.keys():
            even_count[e] += 1
        else:
            even_count[e] = 1
    for o in odd:
        if o in odd_count.keys():
            odd_count[o] += 1
        else:
            odd_count[o] = 1
    if len(even_count.keys()) == 1 and len(odd_count.keys()) == 1:
        if even_count.keys() == odd_count.keys():
            print(n // 2)
        else:
            print(0)
    elif len(even_count.keys()) == 1 and len(odd_count.keys()) == 2:
        if even_count.keys() == odd_count.keys():
            print(n // 2)
        else:
            print(0)
    elif len(even_count.keys()) == 2 and len(odd_count.keys()) == 1:
        if even_count.keys() == odd_count.keys():
            print(n // 2)
        else:
            print(0)
    else:
        even_max = max(even_count.values())
        odd_max = max(odd_count.values())
        even_max_key = 0
        odd_max_key = 0
        for key, value in even_count.items():
            if value == even_max:
                even_max_key = key
        for key, value in odd_count.items():
            if value == odd_max:
                odd_max_key = key
        if even_max_key == odd_max_key:
            even_max2 = 0
            odd_max2 = 0
            for key, value in even_count.items():
                if key != even_max_key:
                    even_max2 = max(even_max2, value)
            for key, value in odd_count.items():
                if key != odd_max_key:
                    odd_max2 = max(odd_max2, value)
            print(n - even_max - odd_max2)
        else:
            print(n - even_max - odd_max)

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(len(even))
        else:
            print(0)
    elif len(set(even)) == 1:
        print(len(odd) - odd.count(even[0]))
    elif len(set(odd)) == 1:
        print(len(even) - even.count(odd[0]))
    else:
        print(min(len(odd) - odd.count(even[0]), len(even) - even.count(odd[0])))

=======
Suggestion 10

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    if c1.most_common()[0][0] != c2.most_common()[0][0]:
        print(n - c1.most_common()[0][1] - c2.most_common()[0][1])
    else:
        print(min(n - c1.most_common()[1][1] - c2.most_common()[0][1], n - c1.most_common()[0][1] - c2.most_common()[1][1]))
