Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    if c1.most_common()[0][0] == c2.most_common()[0][0]:
        if len(c1) == 1 and len(c2) == 1:
            print(n//2)
        elif len(c1) == 1:
            print(n//2-c2.most_common()[1][1])
        elif len(c2) == 1:
            print(n//2-c1.most_common()[1][1])
        else:
            print(n-max(c1.most_common()[1][1]+c2.most_common()[0][1], c1.most_common()[0][1]+c2.most_common()[1][1]))
    else:
        print(n-c1.most_common()[0][1]-c2.most_common()[0][1])
main()

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = [v[i] for i in range(0, n, 2)]
    v2 = [v[i] for i in range(1, n, 2)]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    if len(c1) == 1 and len(c2) == 1:
        if c1.most_common()[0][0] == c2.most_common()[0][0]:
            print(n // 2)
        else:
            print(0)
    else:
        a1 = c1.most_common()[0][1]
        a2 = c2.most_common()[0][1]
        if c1.most_common()[0][0] == c2.most_common()[0][0]:
            if len(c1) == 1:
                print(n // 2 - a2)
            elif len(c2) == 1:
                print(n // 2 - a1)
            else:
                print(n - max(a1 + a2, a1 + a2))
        else:
            print(n - a1 - a2)

=======
Suggestion 3

def main():
    N = int(input())
    V = list(map(int, input().split()))
    A = V[0::2]
    B = V[1::2]
    import collections
    c1 = collections.Counter(A)
    c2 = collections.Counter(B)
    if c1.most_common()[0][0] == c2.most_common()[0][0]:
        if len(c1) == 1 and len(c2) == 1:
            print(N//2)
        else:
            print(N//2 - max(c1.most_common()[0][1], c2.most_common()[0][1]))
    else:
        print(N - c1.most_common()[0][1] - c2.most_common()[0][1])
main()

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = []
    v2 = []
    for i in range(n):
        if i % 2 == 0:
            v1.append(v[i])
        else:
            v2.append(v[i])
    v1_count = [v1.count(i) for i in set(v1)]
    v2_count = [v2.count(i) for i in set(v2)]
    if len(set(v1)) == 1 and len(set(v2)) == 1:
        if v1[0] == v2[0]:
            print(n // 2)
        else:
            print(0)
    elif len(set(v1)) == 1:
        if v1[0] == v2[0]:
            print(n // 2)
        else:
            print(n // 2 - v2_count[0])
    elif len(set(v2)) == 1:
        if v1[0] == v2[0]:
            print(n // 2)
        else:
            print(n // 2 - v1_count[0])
    else:
        print(n - max(v1_count) - max(v2_count))

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = [0] * 100001
    odd = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    even_max = 0
    even_max2 = 0
    even_max_index = 0
    even_max2_index = 0
    odd_max = 0
    odd_max2 = 0
    odd_max_index = 0
    odd_max2_index = 0
    for i in range(100001):
        if even_max < even[i]:
            even_max2 = even_max
            even_max2_index = even_max_index
            even_max = even[i]
            even_max_index = i
        elif even_max2 < even[i]:
            even_max2 = even[i]
            even_max2_index = i
        if odd_max < odd[i]:
            odd_max2 = odd_max
            odd_max2_index = odd_max_index
            odd_max = odd[i]
            odd_max_index = i
        elif odd_max2 < odd[i]:
            odd_max2 = odd[i]
            odd_max2_index = i
    if even_max_index != odd_max_index:
        print(n - even_max - odd_max)
    else:
        print(min(n - even_max - odd_max2, n - even_max2 - odd_max))

=======
Suggestion 6

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    count = 0
    for i in range(0, n, 2):
        if v[i] != v[i+1]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    even_cnt = {}
    odd_cnt = {}
    for i in range(n//2):
        even_cnt[even[i]] = even_cnt.get(even[i], 0) + 1
        odd_cnt[odd[i]] = odd_cnt.get(odd[i], 0) + 1
    even_cnt_sorted = sorted(even_cnt.items(), key=lambda x: x[1], reverse=True)
    odd_cnt_sorted = sorted(odd_cnt.items(), key=lambda x: x[1], reverse=True)
    if even_cnt_sorted[0][0] == odd_cnt_sorted[0][0]:
        if len(even_cnt_sorted) == 1 and len(odd_cnt_sorted) == 1:
            print(n//2)
        elif len(even_cnt_sorted) == 1:
            print(n//2 - odd_cnt_sorted[1][1])
        elif len(odd_cnt_sorted) == 1:
            print(n//2 - even_cnt_sorted[1][1])
        else:
            print(min(n//2 - even_cnt_sorted[1][1] - odd_cnt_sorted[0][1], n//2 - even_cnt_sorted[0][1] - odd_cnt_sorted[1][1]))
    else:
        print(n//2 - even_cnt_sorted[0][1] - odd_cnt_sorted[0][1])

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    even_dic = {}
    odd_dic = {}
    for i in range(n//2):
        if even[i] in even_dic:
            even_dic[even[i]] += 1
        else:
            even_dic[even[i]] = 1
        if odd[i] in odd_dic:
            odd_dic[odd[i]] += 1
        else:
            odd_dic[odd[i]] = 1
    even_dic = sorted(even_dic.items(), key=lambda x: x[1], reverse=True)
    odd_dic = sorted(odd_dic.items(), key=lambda x: x[1], reverse=True)
    if even_dic[0][0] == odd_dic[0][0]:
        if len(even_dic) == 1 and len(odd_dic) == 1:
            print(n//2)
        elif len(even_dic) == 1:
            print(n//2 - odd_dic[1][1])
        elif len(odd_dic) == 1:
            print(n//2 - even_dic[1][1])
        else:
            print(n//2 - max(even_dic[1][1] + odd_dic[0][1], even_dic[0][1] + odd_dic[1][1]))
    else:
        print(n//2 - even_dic[0][1] - odd_dic[0][1])

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1c = {}
    v2c = {}
    for i in range(n//2):
        if v1[i] in v1c:
            v1c[v1[i]] += 1
        else:
            v1c[v1[i]] = 1
        if v2[i] in v2c:
            v2c[v2[i]] += 1
        else:
            v2c[v2[i]] = 1
    v1c_sorted = sorted(v1c.items(), key=lambda x: x[1], reverse=True)
    v2c_sorted = sorted(v2c.items(), key=lambda x: x[1], reverse=True)
    if v1c_sorted[0][0] == v2c_sorted[0][0]:
        if len(v1c_sorted) == 1 and len(v2c_sorted) == 1:
            print(n // 2)
        elif len(v1c_sorted) == 1:
            print(n // 2 - v2c_sorted[1][1])
        elif len(v2c_sorted) == 1:
            print(n // 2 - v1c_sorted[1][1])
        else:
            print(min(n // 2 - v1c_sorted[1][1] - v2c_sorted[0][1], n // 2 - v1c_sorted[0][1] - v2c_sorted[1][1]))
    else:
        print(n // 2 - v1c_sorted[0][1] - v2c_sorted[0][1])

=======
Suggestion 10

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = {}
    even = {}
    for i in range(n):
        if i % 2 == 0:
            if v[i] in even:
                even[v[i]] += 1
            else:
                even[v[i]] = 1
        else:
            if v[i] in odd:
                odd[v[i]] += 1
            else:
                odd[v[i]] = 1

    odd = sorted(odd.items(), key=lambda x: x[1], reverse=True)
    even = sorted(even.items(), key=lambda x: x[1], reverse=True)
    if odd[0][0] != even[0][0]:
        print(n - odd[0][1] - even[0][1])
    elif len(odd) == 1 and len(even) == 1:
        print(n // 2)
    elif len(odd) == 1:
        print(n - even[1][1])
    elif len(even) == 1:
        print(n - odd[1][1])
    else:
        print(min(n - odd[0][1] - even[1][1], n - odd[1][1] - even[0][1]))
