Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    h, w, n = map(int, input().split())
    hlist = [0] * h
    wlist = [0] * w
    for i in range(n):
        a, b = map(int, input().split())
        hlist[a-1] += 1
        wlist[b-1] += 1

    hlist = [i for i in range(h) if hlist[i] == 0]
    wlist = [i for i in range(w) if wlist[i] == 0]
    hlist = [i+1 for i in range(h) if hlist[i] != 0]
    wlist = [i+1 for i in range(w) if wlist[i] != 0]
    for i in range(n):
        print(hlist[i], wlist[i])

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def get_input():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return H, W, N, A, B

=======
Suggestion 4

def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a = sorted(set(a))
    b = sorted(set(b))
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i+1
    for i in range(len(b)):
        b_dict[b[i]] = i+1
    for i in range(n):
        print(a_dict[a[i]],b_dict[b[i]])

=======
Suggestion 5

def main():
    H, W, N = map(int, input().split())
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    #print(H, W, N)
    #print(type(H), type(W), type(N))
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(type(A))
    #print(type(B))
    #print(type(A[0]))
    #print(type(B[0]))
    #print(A[0])
    #print(B[0])
    #print(type(A[1]))
    #print(type(B[1]))
    #print(A[1])
    #print(B[1])
    #print(type(A[2]))
    #print(type(B[2]))
    #print(A[2])
    #print(B[2])
    #print(type(A[3]))
    #print(type(B[3]))
    #print(A[3])
    #print(B[3])
    #print(type(A[4]))
    #print(type(B[4]))
    #print(A[4])
    #print(B[4])
    #print(type(A[5]))
    #print(type(B[5]))
    #print(A[5])
    #print(B[5])
    #print(type(A[6]))
    #print(type(B[6]))
    #print(A[6])
    #print(B[6])
    #print(type(A

=======
Suggestion 6

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    rows = [i for i in range(1, H + 1)]
    cols = [i for i in range(1, W + 1)]
    for i in range(N):
        rows.remove(A[i])
        cols.remove(B[i])
    for i in range(N):
        print(rows[i], cols[i])

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [a for a, _ in AB]
    B = [b for _, b in AB]
    A = sorted(set(A))
    B = sorted(set(B))
    A = {a: i + 1 for i, a in enumerate(A)}
    B = {b: i + 1 for i, b in enumerate(B)}
    for a, b in AB:
        print(A[a], B[b])

=======
Suggestion 8

def solve(H, W, N, AB):
    row = [0] * W
    col = [0] * H
    for i in range(N):
        row[AB[i][1]-1] = i+1
        col[AB[i][0]-1] = i+1
    for i in range(W):
        if row[i] == 0:
            row[i] = N+1
    for i in range(H):
        if col[i] == 0:
            col[i] = N+1
    return row, col
