Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(n):
        if i % 2 == 0:
            even.append(v[i])
        else:
            odd.append(v[i])
    from collections import Counter
    even_cnt = Counter(even).most_common()
    odd_cnt = Counter(odd).most_common()
    if even_cnt[0][0] != odd_cnt[0][0]:
        print(n - even_cnt[0][1] - odd_cnt[0][1])
    elif len(even_cnt) == 1 and len(odd_cnt) == 1:
        print(n // 2)
    elif len(even_cnt) == 1:
        print(n // 2 - odd_cnt[1][1])
    elif len(odd_cnt) == 1:
        print(n // 2 - even_cnt[1][1])
    else:
        print(min(n - even_cnt[0][1] - odd_cnt[1][1], n - even_cnt[1][1] - odd_cnt[0][1]))

=======
Suggestion 2

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

    v1_count = {}
    v2_count = {}
    for i in range(len(v1)):
        if v1[i] in v1_count:
            v1_count[v1[i]] += 1
        else:
            v1_count[v1[i]] = 1

        if v2[i] in v2_count:
            v2_count[v2[i]] += 1
        else:
            v2_count[v2[i]] = 1

    v1_max = 0
    v1_max_key = 0
    for key in v1_count:
        if v1_max < v1_count[key]:
            v1_max = v1_count[key]
            v1_max_key = key

    v2_max = 0
    v2_max_key = 0
    for key in v2_count:
        if v2_max < v2_count[key]:
            v2_max = v2_count[key]
            v2_max_key = key

    if v1_max_key == v2_max_key:
        v1_max2 = 0
        v1_max2_key = 0
        for key in v1_count:
            if key != v1_max_key and v1_max2 < v1_count[key]:
                v1_max2 = v1_count[key]
                v1_max2_key = key

        v2_max2 = 0
        v2_max2_key = 0
        for key in v2_count:
            if key != v2_max_key and v2_max2 < v2_count[key]:
                v2_max2 = v2_count[key]
                v2_max2_key = key

        if v1_max2 + v2_max < v2_max2 + v1_max:
            v1_max = v1_max2
        else:
            v2_max = v2_max2

    print(n - v1_max - v2_max)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = max(v1, key=v1.count)
    c2 = max(v2, key=v2.count)
    if c1 == c2:
        if len(set(v1)) == 1:
            v2 = v[2::2]
            c2 = max(v2, key=v2.count)
            print(len([v[i] for i in range(len(v)) if i % 2 == 0 and v[i] != c2]))
        elif len(set(v2)) == 1:
            v1 = v[1::2]
            c1 = max(v1, key=v1.count)
            print(len([v[i] for i in range(len(v)) if i % 2 == 1 and v[i] != c1]))
        else:
            v1 = v[1::2]
            v2 = v[2::2]
            c1 = max(v1, key=v1.count)
            c2 = max(v2, key=v2.count)
            print(len([v[i] for i in range(len(v)) if i % 2 == 0 and v[i] != c2]) + len([v[i] for i in range(len(v)) if i % 2 == 1 and v[i] != c1]))
    else:
        print(len([v[i] for i in range(len(v)) if i % 2 == 0 and v[i] != c1]) + len([v[i] for i in range(len(v)) if i % 2 == 1 and v[i] != c2]))

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))

    even = {}
    odd = {}
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

    even = sorted(even.items(), key=lambda x:x[1], reverse=True)
    odd = sorted(odd.items(), key=lambda x:x[1], reverse=True)
    if even[0][0] != odd[0][0]:
        print(n - even[0][1] - odd[0][1])
    else:
        if len(even) == 1 and len(odd) == 1:
            print(n // 2)
        elif len(even) == 1:
            print(n - odd[1][1])
        elif len(odd) == 1:
            print(n - even[1][1])
        else:
            print(min(n - even[1][1] - odd[0][1], n - even[0][1] - odd[1][1]))

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = v[0::2]
    even = v[1::2]
    odd_count = {}
    even_count = {}
    for i in range(n//2):
        if odd[i] not in odd_count:
            odd_count[odd[i]] = 1
        else:
            odd_count[odd[i]] += 1
        if even[i] not in even_count:
            even_count[even[i]] = 1
        else:
            even_count[even[i]] += 1
    odd_count = sorted(odd_count.items(), key=lambda x:x[1], reverse=True)
    even_count = sorted(even_count.items(), key=lambda x:x[1], reverse=True)
    if odd_count[0][0] != even_count[0][0]:
        print(n - odd_count[0][1] - even_count[0][1])
    elif len(odd_count) == 1 and len(even_count) == 1:
        print(n//2)
    elif len(odd_count) == 1:
        print(n//2 - even_count[1][1])
    elif len(even_count) == 1:
        print(n//2 - odd_count[1][1])
    else:
        print(min(n - odd_count[0][1] - even_count[1][1], n - odd_count[1][1] - even_count[0][1]))

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    even_count = {}
    odd_count = {}
    for i in range(n//2):
        if even[i] in even_count:
            even_count[even[i]] += 1
        else:
            even_count[even[i]] = 1
        if odd[i] in odd_count:
            odd_count[odd[i]] += 1
        else:
            odd_count[odd[i]] = 1
    even_count = sorted(even_count.items(), key=lambda x: x[1], reverse=True)
    odd_count = sorted(odd_count.items(), key=lambda x: x[1], reverse=True)
    if even_count[0][0] == odd_count[0][0]:
        if len(even_count) == 1 and len(odd_count) == 1:
            print(n//2)
        elif len(even_count) == 1:
            print(n//2 - odd_count[1][1])
        elif len(odd_count) == 1:
            print(n//2 - even_count[1][1])
        else:
            print(min(n//2 - even_count[1][1] - odd_count[0][1], n//2 - even_count[0][1] - odd_count[1][1]))
    else:
        print(n//2 - even_count[0][1] - odd_count[0][1])

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = [0]*10**5
    c2 = [0]*10**5
    for i in range(n//2):
        c1[v1[i]-1] += 1
        c2[v2[i]-1] += 1
    m1 = max(c1)
    m2 = max(c2)
    if c1.index(m1) == c2.index(m2):
        m1 = max(c1[0:c1.index(m1)]+[0]+c1[c1.index(m1)+1:])
        m2 = max(c2[0:c2.index(m2)]+[0]+c2[c2.index(m2)+1:])
    print(n - m1 - m2)

main()

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_even = v[0::2]
    v_odd = v[1::2]
    v_even.sort()
    v_odd.sort()
    v_even_max = max(v_even, key=v_even.count)
    v_odd_max = max(v_odd, key=v_odd.count)
    if v_even_max != v_odd_max:
        print(n - v_even.count(v_even_max) - v_odd.count(v_odd_max))
    else:
        if v_even.count(v_even_max) > v_odd.count(v_odd_max):
            print(n - v_even.count(v_even_max) - v_odd.count(v_odd_max))
        else:
            print(n - v_even.count(v_even_max) - v_odd.count(v_odd_max) + 1)

main()

=======
Suggestion 9

def main():
    N = int(input())
    V = list(map(int, input().split()))

    even = V[0::2]
    odd = V[1::2]

    even_count = {}
    odd_count = {}

    for e in even:
        if e in even_count:
            even_count[e] += 1
        else:
            even_count[e] = 1

    for o in odd:
        if o in odd_count:
            odd_count[o] += 1
        else:
            odd_count[o] = 1

    even_count = sorted(even_count.items(), key=lambda x:x[1], reverse=True)
    odd_count = sorted(odd_count.items(), key=lambda x:x[1], reverse=True)

    # print(even_count)
    # print(odd_count)

    if even_count[0][0] != odd_count[0][0]:
        print(N - even_count[0][1] - odd_count[0][1])
    elif len(even_count) == 1 and len(odd_count) == 1:
        print(N//2)
    elif len(even_count) == 1:
        print(N//2 - odd_count[1][1])
    elif len(odd_count) == 1:
        print(N//2 - even_count[1][1])
    else:
        print(min(N - even_count[0][1] - odd_count[1][1], N - even_count[1][1] - odd_count[0][1]))

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    v = list(map(int, input().split()))
    odd = [0] * 100005
    even = [0] * 100005
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
        print(min(n - even_max - odd[odd_max], n - odd_max - even[even_max]))
    else:
        if even_max > odd_max:
            even[even_max] = 0
            odd[odd_max] = 0
            print(n - even_max - odd[odd_max])
        else:
            even[even_max] = 0
            odd[odd_max] = 0
            print(n - odd_max - even[even_max])
