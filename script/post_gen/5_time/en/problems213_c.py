Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(list(set(A)))
    B = sorted(list(set(B)))
    A_dict = {}
    B_dict = {}
    for i in range(len(A)):
        A_dict[A[i]] = i+1
    for i in range(len(B)):
        B_dict[B[i]] = i+1
    for i in range(N):
        print(A_dict[A[i]], B_dict[B[i]])

=======
Suggestion 2

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)
    #print(H)
    #print(W)
    #print(N)

    #print("")

    #print(max(A))
    #print(max(B))

    #print("")

    #print(min(A))
    #print(min(B))

    #print("")

    #print(max(A) - min(A) + 1)
    #print(max(B) - min(B) + 1)

    #print("")

    #print(H - (max(A) - min(A) + 1))
    #print(W - (max(B) - min(B) + 1))

    #print("")

    #print(max(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)))

    #print("")

    #print(max(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) - min(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)))

    #print("")

    #print(max(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) - min(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) + 1)

    #print("")

    #print(max(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) - min(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) + 1)

    #print("")

    #print(max(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) - min(H - (max(A) - min(A) + 1), W - (max(B) - min(B) + 1)) + 1

=======
Suggestion 3

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
Suggestion 4

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a_sorted = sorted(list(set(a)))
    b_sorted = sorted(list(set(b)))
    a_dict = dict(zip(a_sorted, range(1, len(a_sorted) + 1)))
    b_dict = dict(zip(b_sorted, range(1, len(b_sorted) + 1)))
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
    c = list(set(a))
    d = list(set(b))
    c.sort()
    d.sort()
    cdi = {}
    for i in range(len(c)):
        cdi[c[i]] = i + 1
    for i in range(len(d)):
        cdi[d[i]] = i + 1
    for i in range(len(a)):
        print(cdi[a[i]], cdi[b[i]])

=======
Suggestion 6

def main():
    h, w, n = map(int, input().split())
    card = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(n):
        a, b = map(int, input().split())
        card[a-1][b-1] = i+1
    print(card)
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()
    for i in range(h):
        for j in range(w):
            if card[i][j] == 0:
                card[i].pop(j)
                card[i].append(0)
                break
    print(card)
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()
    for j in range(w):
        for i in range(h):
            if card[i][j] == 0:
                for k in range(h):
                    card[k][j] = card[k][j+1]
                card[h-1][j] = 0
                break
    print(card)
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    rows = list(range(1, H+1))
    cols = list(range(1, W+1))
    for card in cards:
        if card[0] in rows:
            rows.remove(card[0])
        if card[1] in cols:
            cols.remove(card[1])
    for i in range(N):
        print(rows[i], cols[i])

=======
Suggestion 8

def main():
    H,W,N = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    A = [i[0] for i in AB]
    B = [i[1] for i in AB]
    A_ = sorted(list(set(A)))
    B_ = sorted(list(set(B)))
    A_dic = {}
    B_dic = {}
    for i in range(len(A_)):
        A_dic[A_[i]] = i+1
    for i in range(len(B_)):
        B_dic[B_[i]] = i+1
    for i in range(N):
        print(A_dic[A[i]],B_dic[B[i]])

=======
Suggestion 9

def get_input():
    h,w,n = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    return h,w,n,ab

=======
Suggestion 10

def main():
    pass
