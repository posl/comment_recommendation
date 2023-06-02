Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0 and a[i] % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    if c1.most_common()[0][0] == c2.most_common()[0][0]:
        if len(c1) == 1 and len(c2) == 1:
            print(n//2)
        else:
            print(min(n-c1.most_common()[0][1]-c2.most_common()[1][1], n-c1.most_common()[1][1]-c2.most_common()[0][1]))
    else:
        print(n-c1.most_common()[0][1]-c2.most_common()[0][1])

=======
Suggestion 3

def solve(n, v):
    even = v[0::2]
    odd = v[1::2]
    even_count = 0
    odd_count = 0
    even_max = 0
    odd_max = 0
    for i in range(1, 10**5+1):
        if even.count(i) > even_count:
            even_count = even.count(i)
            even_max = i
        if odd.count(i) > odd_count:
            odd_count = odd.count(i)
            odd_max = i
    if even_max != odd_max:
        return n - even_count - odd_count
    else:
        even_count2 = 0
        odd_count2 = 0
        even_max2 = 0
        odd_max2 = 0
        for i in range(1, 10**5+1):
            if even.count(i) > even_count2 and i != even_max:
                even_count2 = even.count(i)
                even_max2 = i
            if odd.count(i) > odd_count2 and i != odd_max:
                odd_count2 = odd.count(i)
                odd_max2 = i
        if even_count2 > odd_count2:
            return n - even_count - odd_count2
        else:
            return n - even_count2 - odd_count
n = int(input())
v = list(map(int, input().split()))
print(solve(n, v))

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = v[0::2]
    even = v[1::2]
    odd_count = {}
    even_count = {}
    for i in odd:
        if i in odd_count:
            odd_count[i] += 1
        else:
            odd_count[i] = 1
    for i in even:
        if i in even_count:
            even_count[i] += 1
        else:
            even_count[i] = 1
    odd_count_sorted = sorted(odd_count.items(), key=lambda x: x[1], reverse=True)
    even_count_sorted = sorted(even_count.items(), key=lambda x: x[1], reverse=True)
    if odd_count_sorted[0][0] != even_count_sorted[0][0]:
        print(n - odd_count_sorted[0][1] - even_count_sorted[0][1])
    else:
        if len(odd_count_sorted) == 1 and len(even_count_sorted) == 1:
            print(n // 2)
        elif len(odd_count_sorted) == 1:
            print(n - even_count_sorted[0][1])
        elif len(even_count_sorted) == 1:
            print(n - odd_count_sorted[0][1])
        else:
            if odd_count_sorted[1][1] > even_count_sorted[1][1]:
                print(n - odd_count_sorted[1][1] - even_count_sorted[0][1])
            else:
                print(n - odd_count_sorted[0][1] - even_count_sorted[1][1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a1 = a[0::2]
    a2 = a[1::2]

    from collections import Counter
    c1 = Counter(a1).most_common(2)
    c2 = Counter(a2).most_common(2)

    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    elif len(c1) == 1 and len(c2) == 1:
        print(n // 2)
    else:
        print(n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1]))

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = max(v1, key=v1.count)
    c2 = max(v2, key=v2.count)
    if c1 != c2:
        print(n - max(v1.count(c1), v2.count(c2)))
    else:
        print(min(n - v1.count(c1) - v2.count(c2), n - v1.count(c1) - v2.count(c2) - 1))

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))

    #奇数番目と偶数番目に分ける
    odd = [0] * 100001
    even = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1

    #最も多く現れる数字を探す
    max_odd = 0
    max_even = 0
    max_odd_idx = 0
    max_even_idx = 0
    for i in range(100001):
        if max_odd < odd[i]:
            max_odd = odd[i]
            max_odd_idx = i
        if max_even < even[i]:
            max_even = even[i]
            max_even_idx = i

    #最も多く現れる数字が異なる場合は、それらを除いて置換する
    if max_odd_idx != max_even_idx:
        print(n - max_odd - max_even)
    #最も多く現れる数字が同じ場合は、より少なく現れる数字を除いて置換する
    else:
        #最も多く現れる数字を除いた時の最大値を探す
        second_odd = 0
        second_even = 0
        for i in range(100001):
            if i == max_odd_idx:
                continue
            if second_odd < odd[i]:
                second_odd = odd[i]
            if second_even < even[i]:
                second_even = even[i]
        print(n - max(max_odd + second_even, second_odd + max_even))

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = v[0::2]
    even = v[1::2]

    odd_count = {}
    even_count = {}
    for i in range(n//2):
        if odd[i] in odd_count:
            odd_count[odd[i]] += 1
        else:
            odd_count[odd[i]] = 1
        if even[i] in even_count:
            even_count[even[i]] += 1
        else:
            even_count[even[i]] = 1

    odd_max = max(odd_count.values())
    even_max = max(even_count.values())
    if odd_max == even_max:
        if len(odd_count) == 1 and len(even_count) == 1:
            print(n//2)
        else:
            print(n - odd_max - even_max)
    elif odd_max > even_max:
        if len(even_count) == 1:
            print(n - odd_max)
        else:
            print(n - odd_max - even_max)
    else:
        if len(odd_count) == 1:
            print(n - even_max)
        else:
            print(n - odd_max - even_max)

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    from collections import Counter
    ceven = Counter(even)
    codd = Counter(odd)
    if ceven.most_common()[0][0] != codd.most_common()[0][0]:
        print(n - ceven.most_common()[0][1] - codd.most_common()[0][1])
    else:
        print(min(n - ceven.most_common()[1][1] - codd.most_common()[0][1], n - ceven.most_common()[0][1] - codd.most_common()[1][1]))

=======
Suggestion 10

def main():
    n = int(input())
    v = list(map(int, input().split()))

    if n % 2 == 0:
        even_list = v[::2]
        odd_list = v[1::2]
        even_list_1 = sorted(even_list)
        odd_list_1 = sorted(odd_list)
        if even_list_1[0] == even_list_1[-1] and odd_list_1[0] == odd_list_1[-1]:
            print(n // 2)
        elif even_list_1[0] == even_list_1[-1] and odd_list_1[0] != odd_list_1[-1]:
            print(n // 2 - odd_list.count(odd_list_1[-1]))
        elif even_list_1[0] != even_list_1[-1] and odd_list_1[0] == odd_list_1[-1]:
            print(n // 2 - even_list.count(even_list_1[-1]))
        else:
            print(n // 2 - even_list.count(even_list_1[-1]) - odd_list.count(odd_list_1[-1]))
    else:
        print("n is not even")
