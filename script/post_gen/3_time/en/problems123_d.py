Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ABC = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ABC.append(A[i] + B[j] + C[k])
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 2

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = [A[i] + B[j] for i in range(X) for j in range(Y)]
    AB.sort(reverse=True)
    ABC = [AB[i] + C[j] for i in range(min(X*Y, K)) for j in range(Z)]
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 3

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 4

def main():
    X, Y, Z, K = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    lst = []
    for i in range(X):
        for j in range(Y):
            lst.append(A[i] + B[j])
    lst = sorted(lst, reverse=True)
    lst = lst[:K]
    lst2 = []
    for i in range(len(lst)):
        for j in range(Z):
            lst2.append(lst[i] + C[j])
    lst2 = sorted(lst2, reverse=True)
    for i in range(K):
        print(lst2[i])

=======
Suggestion 5

def main():
    X, Y, Z, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 6

def solve():
    X, Y, Z, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for ans in ABC[:K]:
        print(ans)

=======
Suggestion 7

def main():
    import heapq
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = []
    for a in A:
        for b in B:
            AB.append(-a-b)
    heapq.heapify(AB)
    ABC = []
    for i in range(K):
        ab = heapq.heappop(AB)
        for c in C:
            abc = ab - c
            heapq.heappush(ABC, abc)
    for i in range(K):
        print(-heapq.heappop(ABC))

=======
Suggestion 8

def   main (): 
     X ,   Y ,   Z ,   K   =   map ( int ,   input (). split ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     B   =   list ( map ( int ,   input (). split ())) 
     C   =   list ( map ( int ,   input (). split ())) 

     A . sort ( reverse = True ) 
     B . sort ( reverse = True ) 
     C . sort ( reverse = True ) 

     AB   =   [] 
     for   a   in   A : 
         for   b   in   B : 
             AB . append ( a   +   b ) 
     AB . sort ( reverse = True ) 
     ABC   =   [] 
     for   ab   in   AB [: K ]: 
         for   c   in   C : 
             ABC . append ( ab   +   c ) 
     ABC . sort ( reverse = True ) 
     for   abc   in   ABC [: K ]: 
         print ( abc )

=======
Suggestion 9

def solve():
    import heapq
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    q = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if i * j * k < K:
                    heapq.heappush(q, -(A[i] + B[j] + C[k]))
                else:
                    break
    for _ in range(K):
        print(-heapq.heappop(q))

=======
Suggestion 10

def read_int():
    return int(input())
