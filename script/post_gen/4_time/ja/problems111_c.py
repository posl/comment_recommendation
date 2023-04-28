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
    if c1.most_common()[0][0] != c2.most_common()[0][0]:
        print(n - c1.most_common()[0][1] - c2.most_common()[0][1])
    else:
        if len(c1) == 1 and len(c2) == 1:
            print(n // 2)
        elif len(c1) == 1:
            print(n - c2.most_common()[1][1])
        elif len(c2) == 1:
            print(n - c1.most_common()[1][1])
        else:
            print(min(n - c1.most_common()[0][1] - c2.most_common()[1][1], n - c1.most_common()[1][1] - c2.most_common()[0][1]))

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    if n == 2:
        if v[0] == v[1]:
            print(1)
        else:
            print(0)
    else:
        count1 = 0
        count2 = 0
        for i in range(n):
            if i % 2 == 0:
                if v[i] != v[0]:
                    count1 += 1
                if v[i] != v[1]:
                    count2 += 1
            else:
                if v[i] != v[1]:
                    count1 += 1
                if v[i] != v[0]:
                    count2 += 1
        print(min(count1, count2))

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(n):
        if i%2 == 0:
            even.append(v[i])
        else:
            odd.append(v[i])
    even_count = []
    odd_count = []
    for i in range(1, max(v)+1):
        even_count.append(even.count(i))
        odd_count.append(odd.count(i))
    even_max = max(even_count)
    odd_max = max(odd_count)
    if even_count.index(even_max) == odd_count.index(odd_max):
        if even_max == odd_max:
            even_count[even_count.index(even_max)] = 0
            odd_count[odd_count.index(odd_max)] = 0
            even_max = max(even_count)
            odd_max = max(odd_count)
        else:
            even_count[even_count.index(even_max)] = 0
            even_max = max(even_count)
            odd_count[odd_count.index(odd_max)] = 0
            odd_max = max(odd_count)
    even_sum = len(even) - even_max
    odd_sum = len(odd) - odd_max
    print(even_sum + odd_sum)

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    d1 = {}
    d2 = {}
    for i in range(n//2):
        d1[v1[i]] = d1.get(v1[i], 0) + 1
        d2[v2[i]] = d2.get(v2[i], 0) + 1
    if len(d1) == 1 and len(d2) == 1:
        if v1[0] == v2[0]:
            print(n//2)
        else:
            print(0)
    elif len(d1) == 1 or len(d2) == 1:
        if len(d1) == 1:
            d = d1
        else:
            d = d2
        key = list(d.keys())[0]
        value = d[key]
        print(n//2 - value)
    else:
        key1 = list(d1.keys())[0]
        key2 = list(d2.keys())[0]
        value1 = d1[key1]
        value2 = d2[key2]
        if key1 == key2:
            if value1 > value2:
                print(n//2 - value1)
            else:
                print(n//2 - value2)
        else:
            print(n//2 - value1 - value2)

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = {}
    even = {}
    for i in range(n):
        if i % 2 == 0:
            if v[i] not in odd:
                odd[v[i]] = 1
            else:
                odd[v[i]] += 1
        else:
            if v[i] not in even:
                even[v[i]] = 1
            else:
                even[v[i]] += 1
    odd = sorted(odd.items(), key=lambda x: x[1], reverse=True)
    even = sorted(even.items(), key=lambda x: x[1], reverse=True)
    if odd[0][0] != even[0][0]:
        print(n - odd[0][1] - even[0][1])
    else:
        if len(odd) == 1 and len(even) == 1:
            print(int(n / 2))
        elif len(odd) == 1 and len(even) != 1:
            print(n - even[1][1])
        elif len(odd) != 1 and len(even) == 1:
            print(n - odd[1][1])
        else:
            print(min(n - odd[0][1] - even[1][1], n - odd[1][1] - even[0][1]))

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    if c1.most_common()[0][0] != c2.most_common()[0][0]:
        print(n - c1.most_common()[0][1] - c2.most_common()[0][1])
    else:
        if len(c1) == 1 and len(c2) == 1:
            print(n // 2)
        elif len(c1) == 1:
            print(n - c2.most_common()[1][1])
        elif len(c2) == 1:
            print(n - c1.most_common()[1][1])
        else:
            print(min(n - c1.most_common()[1][1] - c2.most_common()[0][1], n - c1.most_common()[0][1] - c2.most_common()[1][1]))

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = 0
    c2 = 0
    v1c = max(v1, key=v1.count)
    v2c = max(v2, key=v2.count)
    for i in range(n//2):
        if v1[i] != v1c:
            c1 += 1
        if v2[i] != v2c:
            c2 += 1
    if v1c != v2c:
        print(c1+c2)
    else:
        if c1 < c2:
            print(c1 + min(c1, c2+1))
        else:
            print(c2 + min(c2, c1+1))

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))

    v1 = v[0::2]
    v2 = v[1::2]

    d1 = {}
    d2 = {}

    for i in range(n//2):
        d1[v1[i]] = d1.get(v1[i], 0) + 1
        d2[v2[i]] = d2.get(v2[i], 0) + 1

    d1_sorted = sorted(d1.items(), key=lambda x: x[1], reverse=True)
    d2_sorted = sorted(d2.items(), key=lambda x: x[1], reverse=True)

    if d1_sorted[0][0] != d2_sorted[0][0]:
        print(n - d1_sorted[0][1] - d2_sorted[0][1])
    else:
        if len(d1_sorted) == 1 and len(d2_sorted) == 1:
            print(n//2)
        elif len(d1_sorted) == 1:
            print(n - d1_sorted[0][1] - d2_sorted[1][1])
        elif len(d2_sorted) == 1:
            print(n - d1_sorted[1][1] - d2_sorted[0][1])
        else:
            print(min(n - d1_sorted[0][1] - d2_sorted[1][1], n - d1_sorted[1][1] - d2_sorted[0][1]))

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v0 = v[::2]
    v1 = v[1::2]
    v0c = []
    v1c = []
    for i in range(1, max(v)+1):
        v0c.append(v0.count(i))
        v1c.append(v1.count(i))
    if v0c.index(max(v0c)) == v1c.index(max(v1c)):
        if len(v0c) == 1:
            print(n//2)
        else:
            print(n-max(v0c)-max(v1c))
    else:
        print(n-max(v0c)-max(v1c))

=======
Suggestion 10

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    m1 = max(set(v1), key=v1.count)
    m2 = max(set(v2), key=v2.count)
    if m1 != m2:
        print(N - v1.count(m1) - v2.count(m2))
    else:
        m1 = max(set(v1), key=v1.count)
        m2 = max(set(v2), key=v2.count)
        print(min(N - v1.count(m1) - v2.count(m2), N - v1.count(m2) - v2.count(m1)))
