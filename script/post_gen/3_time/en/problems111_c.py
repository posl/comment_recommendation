Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     n   =   int ( input ()) 
     v   =   list ( map ( int ,   input (). split ())) 

     v1   =   v [:: 2 ] 
     v2   =   v [ 1 :: 2 ] 

     c1   =   Counter ( v1 ) 
     c2   =   Counter ( v2 ) 

     m1 ,   m2   =   c1 . most_common ( 1 )[ 0 ][ 0 ],   c2 . most_common ( 1 )[ 0 ][ 0 ] 

     if   m1   !=   m2 : 
         print ( n   -   c1 [ m1 ]   -   c2 [ m2 ]) 
     else : 
         m1 ,   m2   =   c1 . most_common ( 2 )[ 1 ][ 0 ],   c2 . most_common ( 2 )[ 1 ][ 0 ] 
         print ( min ( n   -   c1 [ m1 ]   -   c2 [ m2 ],   n   -   c1 [ m2 ]   -   c2 [ m1 ]))

=======
Suggestion 2

def   main (): 
     n   =   int ( input ()) 
     v   =   list ( map ( int ,   input (). split ())) 
     odd   =   v [:: 2 ] 
     even   =   v [ 1 :: 2 ] 

     odd1   =   max ( odd ,   key = odd . count ) 
     odd2   =   max ( odd ,   key = odd . count ,   default = None ) 
     even1   =   max ( even ,   key = even . count ) 
     even2   =   max ( even ,   key = even . count ,   default = None ) 

     if   odd1   !=   odd2   and   even1   !=   even2 : 
         print ( n   -   max ( odd . count ( odd1 ),   odd . count ( odd2 ),   even . count ( even1 ),   even . count ( even2 ))) 
     elif   odd1   ==   odd2   and   even1   ==   even2 : 
         print ( n   //   2 ) 
     elif   odd1   ==   odd2 : 
         print ( n   -   max ( odd . count ( odd1 ),   even . count ( even1 ),   even . count ( even2 ))) 
     else : 
         print ( n   -   max ( odd . count ( odd1 ),   odd . count ( odd2 ),   even . count ( even1 )))

=======
Suggestion 3

def main():
    N = int(input())
    V = list(map(int, input().split()))
    A, B = [], []
    for i in range(N):
        if i % 2 == 0:
            A.append(V[i])
        else:
            B.append(V[i])
    A.sort()
    B.sort()
    A.append(0)
    B.append(0)
    if A[0] == A[-2]:
        a = A[-1]
    else:
        a = A[0]
    if B[0] == B[-2]:
        b = B[-1]
    else:
        b = B[0]
    if a == b:
        if A.count(A[0]) > B.count(B[0]):
            print(N - A.count(A[0]))
        else:
            print(N - B.count(B[0]))
    else:
        print(N - A.count(a) - B.count(b))

=======
Suggestion 4

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
    elif v2[0] == v2[-1]:
        print(n//2 - v1.count(v1[0]))
    else:
        print(n//2 - v1.count(v1[0]) + n//2 - v2.count(v2[0]))

=======
Suggestion 5

def main():
    N = int(input())
    V = list(map(int, input().split()))
    V1 = V[::2]
    V2 = V[1::2]
    V1.sort()
    V2.sort()
    if V1[0] == V1[-1]:
        if V2[0] == V2[-1]:
            print((N//2))
        else:
            print((N//2)-V2.count(V2[0]))
    elif V2[0] == V2[-1]:
        print((N//2)-V1.count(V1[0]))
    else:
        print(min((N//2)-V1.count(V1[0])+(N//2)-V2.count(V2[0]),(N//2)-V1.count(V1[-1])+(N//2)-V2.count(V2[-1])))

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    even_c = Counter(even)
    odd_c = Counter(odd)
    even_max = even_c.most_common()[0]
    odd_max = odd_c.most_common()[0]
    if even_max[0] == odd_max[0]:
        if len(even_c) == 1 or len(odd_c) == 1:
            print(n // 2)
        else:
            even_max2 = even_c.most_common()[1]
            odd_max2 = odd_c.most_common()[1]
            print(min(n - even_max[1] - odd_max2[1], n - even_max2[1] - odd_max[1]))
    else:
        print(n - even_max[1] - odd_max[1])

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    #print(v)
    v1 = v[::2]
    v2 = v[1::2]
    #print(v1)
    #print(v2)
    v1.sort()
    v2.sort()
    #print(v1)
    #print(v2)
    v1c = [0] * (10 ** 5 + 1)
    v2c = [0] * (10 ** 5 + 1)
    for i in range(n):
        if i % 2 == 0:
            v1c[v1[i]] += 1
        else:
            v2c[v2[i]] += 1
    #print(v1c)
    #print(v2c)
    v1m = v1c.index(max(v1c))
    v2m = v2c.index(max(v2c))
    #print(v1m)
    #print(v2m)
    if v1m == v2m:
        v1m2 = v1c.index(sorted(v1c, reverse = True)[1])
        v2m2 = v2c.index(sorted(v2c, reverse = True)[1])
        if v1c[v1m] + v2c[v2m2] > v1c[v1m2] + v2c[v2m]:
            print(n - v1c[v1m] - v2c[v2m2])
        else:
            print(n - v1c[v1m2] - v2c[v2m])
    else:
        print(n - v1c[v1m] - v2c[v2m])

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[::2]
    b = v[1::2]
    c = [0] * 10**5
    d = [0] * 10**5
    for i in a:
        c[i-1] += 1
    for j in b:
        d[j-1] += 1
    e = c.index(max(c))
    f = d.index(max(d))
    if e == f:
        g = c.index(sorted(c)[-2])
        h = d.index(sorted(d)[-2])
        print(min(n-c[e]-d[h], n-c[g]-d[f]))
    else:
        print(n-c[e]-d[f])

=======
Suggestion 9

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = [0] * 100001
    for v in V:
        C[v] += 1
    V.sort()
    V = V[N//2:]
    if V[0] == V[-1]:
        print(N//2)
    else:
        print(N - max(C[V[0]], C[V[-1]]))

=======
Suggestion 10

def read_ints():
    return map(int, input().split())
