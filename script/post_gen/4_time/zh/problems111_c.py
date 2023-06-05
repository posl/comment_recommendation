Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1).most_common()
    c2 = Counter(v2).most_common()
    if len(c1) == 1 and len(c2) == 1:
        if c1[0][0] == c2[0][0]:
            print(n//2)
        else:
            print(0)
    elif len(c1) == 1:
        print(n//2-c2[0][1])
    elif len(c2) == 1:
        print(n//2-c1[0][1])
    else:
        print(n-c1[0][1]-c2[0][1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # print(n)
    count = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 != 0:
                count += 1
        else:
            if a[i] % 2 == 0:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    if c1.most_common()[0][0] != c2.most_common()[0][0]:
        print(n-c1.most_common()[0][1]-c2.most_common()[0][1])
    elif len(c1) == 1:
        print(n//2)
    elif len(c1) == 2:
        print(n//2 - min(c1.most_common()[0][1], c2.most_common()[1][1]))
    else:
        print(n//2 - c1.most_common()[1][1])

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int,input().split()))
    a = v[0::2]
    b = v[1::2]
    from collections import Counter
    a = Counter(a).most_common(2)
    b = Counter(b).most_common(2)
    if a[0][0] != b[0][0]:
        print(n-a[0][1]-b[0][1])
    else:
        if len(a) == 1 and len(b) == 1:
            print(n//2)
        elif len(a) == 1:
            print(n-b[1][1])
        elif len(b) == 1:
            print(n-a[1][1])
        else:
            print(min(n-a[1][1]-b[0][1],n-a[0][1]-b[1][1]))

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if i % 2 == 0:
            if v[i] not in d:
                d[v[i]] = 0
            d[v[i]] += 1
        else:
            if v[i] not in d:
                d[v[i]] = 0
            d[v[i]] -= 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(len(d)):
        if i == 2:
            break
        ans += d[i][1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1).most_common()
    c2 = Counter(v2).most_common()
    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    elif len(c1) == 1 and len(c2) == 1:
        print(n // 2)
    else:
        print(n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1]))

=======
Suggestion 7

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

    even_max1 = 0
    even_max2 = 0
    even_max1_index = 0
    even_max2_index = 0
    odd_max1 = 0
    odd_max2 = 0
    odd_max1_index = 0
    odd_max2_index = 0
    for i in range(100001):
        if even_max1 < even[i]:
            even_max2 = even_max1
            even_max2_index = even_max1_index
            even_max1 = even[i]
            even_max1_index = i
        elif even_max2 < even[i]:
            even_max2 = even[i]
            even_max2_index = i
        if odd_max1 < odd[i]:
            odd_max2 = odd_max1
            odd_max2_index = odd_max1_index
            odd_max1 = odd[i]
            odd_max1_index = i
        elif odd_max2 < odd[i]:
            odd_max2 = odd[i]
            odd_max2_index = i

    if even_max1_index != odd_max1_index:
        print(n - even_max1 - odd_max1)
    else:
        print(min(n - even_max1 - odd_max2, n - even_max2 - odd_max1))

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    v1c = {}
    v2c = {}
    for i in v1:
        if i in v1c:
            v1c[i] += 1
        else:
            v1c[i] = 1
    for i in v2:
        if i in v2c:
            v2c[i] += 1
        else:
            v2c[i] = 1
    v1c = sorted(v1c.items(), key=lambda x: x[1], reverse=True)
    v2c = sorted(v2c.items(), key=lambda x: x[1], reverse=True)
    if v1c[0][0] != v2c[0][0]:
        print(n - v1c[0][1] - v2c[0][1])
    elif len(v1c) == 1 and len(v2c) == 1:
        print(n // 2)
    elif len(v1c) == 1:
        print(n - v1c[0][1] - v2c[1][1])
    elif len(v2c) == 1:
        print(n - v1c[1][1] - v2c[0][1])
    else:
        print(min(n - v1c[0][1] - v2c[1][1], n - v1c[1][1] - v2c[0][1]))

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(n // 2)
        else:
            print(0)
    elif len(set(even)) == 1:
        print(n // 2 - odd.count(even[0]))
    elif len(set(odd)) == 1:
        print(n // 2 - even.count(odd[0]))
    else:
        print(min(n // 2 - even.count(max(set(even), key=even.count)), n // 2 - odd.count(max(set(odd), key=odd.count))))
main()

=======
Suggestion 10

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(n // 2)
        else:
            print(0)
    elif len(set(even)) == 1:
        print(n // 2)
    elif len(set(odd)) == 1:
        print(n // 2)
    else:
        print(min(even.count(odd[0]) + odd.count(even[0]), even.count(odd[1]) + odd.count(even[1])))
