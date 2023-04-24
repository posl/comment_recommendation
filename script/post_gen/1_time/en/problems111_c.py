Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    t1 = c1.most_common()
    t2 = c2.most_common()
    if t1[0][0] != t2[0][0]:
        print(n - t1[0][1] - t2[0][1])
    else:
        if len(t1) == 1:
            print(n - t2[1][1])
        elif len(t2) == 1:
            print(n - t1[1][1])
        else:
            print(n - max(t1[0][1] + t2[1][1], t1[1][1] + t2[0][1]))

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1.sort()
    v2.sort()
    if v1[0] == v1[-1]:
        if v2[0] == v2[-1]:
            print(n//2)
        else:
            print(n//2 - v2.count(v2[0]))
    else:
        if v2[0] == v2[-1]:
            print(n//2 - v1.count(v1[0]))
        else:
            print(min(n//2 - v1.count(v1[0]), n//2 - v2.count(v2[0])))

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1.sort()
    v2.sort()
    v1.append(0)
    v2.append(0)
    if v1[-2] == v2[-2]:
        if v1[-3] == v2[-3]:
            print(min(n-v1.count(v1[-2]), n-v2.count(v2[-2])))
        else:
            print(min(n-v1.count(v1[-2]), n-v2.count(v2[-3])))
    else:
        print(min(n-v1.count(v1[-2]), n-v2.count(v2[-2])))

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = sorted([(v1.count(i), i) for i in set(v1)], reverse=True)
    c2 = sorted([(v2.count(i), i) for i in set(v2)], reverse=True)
    if c1[0][1] != c2[0][1]:
        print(n - c1[0][0] - c2[0][0])
    else:
        print(min(n - c1[0][0] - c2[1][0], n - c1[1][0] - c2[0][0]))

=======
Suggestion 5

def solve():
    N = int(input())
    V = list(map(int, input().split()))
    V1 = V[::2]
    V2 = V[1::2]
    V1.sort()
    V2.sort()
    if V1[0] == V1[-1]:
        if V2[0] == V2[-1]:
            print(0)
        else:
            print(N//2 - V2.count(V2[0]))
    elif V2[0] == V2[-1]:
        print(N//2 - V1.count(V1[0]))
    else:
        print(N//2 - V1.count(V1[0]) + N//2 - V2.count(V2[0]))

=======
Suggestion 6

def main():
    N = int(input())
    V = list(map(int, input().split()))
    A = V[0::2]
    B = V[1::2]
    import collections
    C = collections.Counter(A)
    D = collections.Counter(B)
    E = C.most_common()
    F = D.most_common()
    if E[0][0] == F[0][0]:
        if len(E) == 1 and len(F) == 1:
            print(N//2)
        elif len(E) == 1:
            print(N - F[0][1] - F[1][1])
        elif len(F) == 1:
            print(N - E[0][1] - E[1][1])
        else:
            print(N - max(E[0][1] + F[1][1], E[1][1] + F[0][1]))
    else:
        print(N - E[0][1] - F[0][1])

=======
Suggestion 7

def main():
    N = int(input())
    V = list(map(int, input().split()))
    if N == 2:
        print(0)
        return
    even = V[::2]
    odd = V[1::2]
    even_c = Counter(even)
    odd_c = Counter(odd)
    even_max = even_c.most_common()[0]
    odd_max = odd_c.most_common()[0]
    if even_max[0] == odd_max[0]:
        if len(even_c) == 1:
            even_max = even_c.most_common()[1]
        elif len(odd_c) == 1:
            odd_max = odd_c.most_common()[1]
        else:
            even_max = even_c.most_common()[1]
            odd_max = odd_c.most_common()[1]
    print(N - even_max[1] - odd_max[1])

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    
    even = v[::2]
    odd = v[1::2]
    
    even_dic = {}
    odd_dic = {}
    
    for i in even:
        if i in even_dic:
            even_dic[i] += 1
        else:
            even_dic[i] = 1
    
    for i in odd:
        if i in odd_dic:
            odd_dic[i] += 1
        else:
            odd_dic[i] = 1
    
    even_max = max(even_dic, key=even_dic.get)
    odd_max = max(odd_dic, key=odd_dic.get)
    
    if even_max == odd_max:
        even_max_num = even_dic[even_max]
        odd_max_num = odd_dic[odd_max]
        
        del even_dic[even_max]
        del odd_dic[odd_max]
        
        even_max2 = max(even_dic, key=even_dic.get)
        odd_max2 = max(odd_dic, key=odd_dic.get)
        
        even_max2_num = even_dic[even_max2]
        odd_max2_num = odd_dic[odd_max2]
        
        print(min(n - even_max2_num - odd_max_num, n - even_max_num - odd_max2_num))
    else:
        print(n - even_dic[even_max] - odd_dic[odd_max])

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [A[i] for i in range(0, len(A), 2)]
    C = [A[i] for i in range(1, len(A), 2)]
    from collections import Counter
    B = Counter(B)
    C = Counter(C)
    B = B.most_common()
    C = C.most_common()
    if B[0][0] != C[0][0]:
        print(N - B[0][1] - C[0][1])
    else:
        if len(B) == 1:
            print(N - C[1][1])
        elif len(C) == 1:
            print(N - B[1][1])
        else:
            print(N - max(B[0][1] + C[1][1], B[1][1] + C[0][1]))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = n
    for i in range(2):
        b = a[i::2]
        c = a[1-i::2]
        d = sorted(b + c)
        e = d[0]
        f = d[-1]
        if e != f:
            ans = min(ans, b.count(e) + c.count(f))
    print(ans)
