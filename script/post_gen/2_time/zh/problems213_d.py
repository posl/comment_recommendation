Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h,w,n = map(int,input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int,input().split())))
    for i in range(n):
        cards[i].append(i+1)
    cards.sort(key=lambda x:x[1])
    cards.sort(key=lambda x:x[0])
    for i in range(n):
        print(cards[i][2],cards[i][0],cards[i][1])

=======
Suggestion 3

def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_index = {}
    b_index = {}
    for i in range(len(a)):
        a_index[a[i]] = i+1
    for i in range(len(b)):
        b_index[b[i]] = i+1
    for i in range(n):
        print(a_index[a[i]],b_index[b[i]])

=======
Suggestion 4

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a_sorted[i]] = i + 1
        b_dict[b_sorted[i]] = i + 1
    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])

=======
Suggestion 5

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()

    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i + 1
    for i in range(len(b)):
        b_dict[b[i]] = i + 1

    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])

=======
Suggestion 6

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(A)
    B = sorted(B)
    C = []
    D = []
    for i in range(N):
        if i == 0:
            C.append(A[i])
            D.append(B[i])
        else:
            if A[i] != A[i-1]:
                C.append(A[i])
            if B[i] != B[i-1]:
                D.append(B[i])
    for i in range(N):
        print(C.index(A[i])+1, D.index(B[i])+1)

=======
Suggestion 7

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a = {a[i]:i+1 for i in range(len(a))}
    b = {b[i]:i+1 for i in range(len(b))}
    for i in range(n):
        print(a[a[i+1]], b[b[i+1]])

=======
Suggestion 8

def solve(h, w, n, ab):
    a = []
    b = []
    for i in range(n):
        a.append(ab[i][0])
        b.append(ab[i][1])
    a.sort()
    b.sort()
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i+1
    for i in range(len(b)):
        b_dict[b[i]] = i+1
    for i in range(n):
        print(a_dict[ab[i][0]], b_dict[ab[i][1]])
