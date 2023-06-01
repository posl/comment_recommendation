Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    print(min(replace(v, 0), replace(v, 1)))

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even, odd = v[::2], v[1::2]
    even_cnt = dict()
    odd_cnt = dict()
    for i in range(n//2):
        even_cnt[even[i]] = even_cnt.get(even[i], 0) + 1
        odd_cnt[odd[i]] = odd_cnt.get(odd[i], 0) + 1
    even_cnt = sorted(even_cnt.items(), key=lambda x:x[1], reverse=True)
    odd_cnt = sorted(odd_cnt.items(), key=lambda x:x[1], reverse=True)
    if even_cnt[0][0] != odd_cnt[0][0]:
        print(n - even_cnt[0][1] - odd_cnt[0][1])
    else:
        if len(even_cnt) == 1 and len(odd_cnt) == 1:
            print(n//2)
        elif len(even_cnt) == 1:
            print(n//2 - odd_cnt[1][1])
        elif len(odd_cnt) == 1:
            print(n//2 - even_cnt[1][1])
        else:
            print(min(n - even_cnt[0][1] - odd_cnt[1][1], n - even_cnt[1][1] - odd_cnt[0][1]))

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = [0] * 100001
    even = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    even_max = max(even)
    odd_max = max(odd)
    if even_max == odd_max:
        even[even_max] = 0
        odd[odd_max] = 0
        print(n - max(max(even), max(odd)))
    else:
        print(n - even_max - odd_max)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if a[i-1] == a[i+1] and a[i-1] != a[i]:
            ans += 1
            a[i] = a[i-1]
    print(ans)

=======
Suggestion 5

def min_replace_count(n, v):
    # 通过排序找出最小值和最大值
    v = sorted(v)
    # 最小值和最大值相等，说明所有元素都相等，无法构造/\/\/\/
    if v[0] == v[-1]:
        return n // 2
    # 最小值和最大值不相等，说明可以构造/\/\/\/
    else:
        # 构造/\/\/\/需要替换的元素个数
        return n // 2 - v.count(v[0])

=======
Suggestion 6

def solve(n, v):
    odd = v[::2]
    even = v[1::2]
    from collections import Counter
    odd_cnt = Counter(odd).most_common()
    even_cnt = Counter(even).most_common()
    if len(odd_cnt) == 1 and len(even_cnt) == 1:
        if odd_cnt[0][0] == even_cnt[0][0]:
            return n // 2
        else:
            return 0
    if len(odd_cnt) == 1:
        return n // 2 - even_cnt[0][1]
    if len(even_cnt) == 1:
        return n // 2 - odd_cnt[0][1]
    return n - odd_cnt[0][1] - even_cnt[0][1]

=======
Suggestion 7

def check(l):
    if len(l) % 2 != 0:
        return False
    if len(l) == 2:
        return False
    if len(l) == 4:
        if l[0] == l[2] and l[1] == l[3] and l[0] != l[1]:
            return True
        else:
            return False
    if len(l) > 4:
        if l[0] == l[2] and l[1] == l[3] and l[0] != l[1]:
            return check(l[2:])
        else:
            return False

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]

    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(len(v) // 2)
        else:
            print(0)
    else:
        if len(set(even)) == 1:
            print(len(v) // 2 - odd.count(even[0]))
        elif len(set(odd)) == 1:
            print(len(v) // 2 - even.count(odd[0]))
        else:
            print(len(v) // 2 - max(odd.count(max(set(odd), key=odd.count)), even.count(max(set(even), key=even.count))))

=======
Suggestion 9

def solve(n, v):
    ans = 0
    for i in range(0, n, 2):
        if v[i] == v[i+1]:
            ans += 1
    return ans

=======
Suggestion 10

def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[::2]
    b = v[1::2]
    from collections import Counter
    a_c = Counter(a).most_common()
    b_c = Counter(b).most_common()
    if a_c[0][0] != b_c[0][0]:
        print(n - a_c[0][1] - b_c[0][1])
    else:
        if len(a_c) == 1 and len(b_c) == 1:
            print(n // 2)
        elif len(a_c) == 1:
            print(n - b_c[1][1])
        elif len(b_c) == 1:
            print(n - a_c[1][1])
        else:
            print(n - max(a_c[0][1] + b_c[1][1], a_c[1][1] + b_c[0][1]))
