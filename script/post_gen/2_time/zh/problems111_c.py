Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int,input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    c1_most = c1.most_common(2)
    c2_most = c2.most_common(2)
    if c1_most[0][0] != c2_most[0][0]:
        print(n-c1_most[0][1]-c2_most[0][1])
    elif len(c1_most) == 1 and len(c2_most) == 1:
        print(n//2)
    elif len(c1_most) == 1:
        print(n-c2_most[0][1]-c2_most[1][1])
    elif len(c2_most) == 1:
        print(n-c1_most[0][1]-c1_most[1][1])
    else:
        print(min(n-c1_most[0][1]-c2_most[1][1],n-c1_most[1][1]-c2_most[0][1]))

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] == a[0]:
                ans += 1
        else:
            if a[i] == a[1]:
                ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    v = list(map(int,input().split()))
    even = [0] * 100001
    odd = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    even_max = max(even)
    odd_max = max(odd)
    if even_max == odd_max:
        even[0] = 0
        odd[0] = 0
        even_max2 = max(even)
        odd_max2 = max(odd)
        print(n - max(even_max + odd_max2, even_max2 + odd_max))
    else:
        print(n - even_max - odd_max)

=======
Suggestion 4

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
            print(n // 2)
        else:
            print(min(n - c1.most_common()[0][1] - c2.most_common()[1][1],
                      n - c1.most_common()[1][1] - c2.most_common()[0][1]))
    else:
        print(n - c1.most_common()[0][1] - c2.most_common()[0][1])

=======
Suggestion 5

def solve(n,vs):
    if n == 2:
        if vs[0] != vs[1]:
            return 0
        else:
            return 1
    else:
        count = 0
        for i in range(0,n,2):
            if vs[i] == vs[i+1]:
                count += 1
        return count

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = [v1.count(i) for i in set(v1)]
    c2 = [v2.count(i) for i in set(v2)]
    if len(set(v1)) == 1 and len(set(v2)) == 1:
        if v1[0] == v2[0]:
            print(n//2)
        else:
            print(0)
    elif len(set(v1)) == 1 and len(set(v2)) != 1:
        if v1[0] == v2[c2.index(max(c2))]:
            print(n//2 - max(c2))
        else:
            print(n//2 - max(c2) - 1)
    elif len(set(v1)) != 1 and len(set(v2)) == 1:
        if v2[0] == v1[c1.index(max(c1))]:
            print(n//2 - max(c1))
        else:
            print(n//2 - max(c1) - 1)
    else:
        if v1[c1.index(max(c1))] == v2[c2.index(max(c2))]:
            c1[c1.index(max(c1))] = 0
            c2[c2.index(max(c2))] = 0
            if max(c1) > max(c2):
                print(n//2 - max(c1) - max(c2))
            else:
                print(n//2 - max(c1) - max(c2) - 1)
        else:
            print(n//2 - max(c1) - max(c2))

main()

=======
Suggestion 7

def find_min_change_num(n, v):
    min_change_num = n
    for i in range(2):
        cnt = 0
        for j in range(i, n, 2):
            if v[j] != v[i]:
                cnt += 1
        min_change_num = min(min_change_num, cnt)
    return min_change_num

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1).most_common(2)
    c2 = Counter(v2).most_common(2)
    c1.append((0, 0))
    c2.append((0, 0))
    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    else:
        print(n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1]))

=======
Suggestion 9

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(0, n, 2):
        if v[i] == v[i+1]:
            ans += 1
    print(ans)
solve()

=======
Suggestion 10

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v0 = v[::2]
    v1 = v[1::2]
    from collections import Counter
    c0 = Counter(v0)
    c1 = Counter(v1)
    if c0.most_common()[0][0] != c1.most_common()[0][0]:
        print(n - c0.most_common()[0][1] - c1.most_common()[0][1])
    else:
        if len(c0) == 1:
            print(n // 2)
        else:
            c0.most_common()[1][1] = 0
            c1.most_common()[1][1] = 0
            print(n - max(c0.most_common()[1][1] + c1.most_common()[0][1], c0.most_common()[0][1] + c1.most_common()[1][1]))
    return
