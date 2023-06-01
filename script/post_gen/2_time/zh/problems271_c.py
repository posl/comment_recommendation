Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(q):
        a.append(list(map(int, input().split())))
    for i in range(q):
        print(l[a[i][0]-1][a[i][1]-1])

main()

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])
main()

=======
Suggestion 4

def get_input():
    n, q = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    s_t = []
    for i in range(q):
        s_t.append(list(map(int, input().split())))
    return n, q, l, s_t

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split()))[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))

    for i in range(q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 8

def get_list():
    N, Q = input().split()
    N = int(N)
    Q = int(Q)
    list_N = []
    for i in range(N):
        list_N.append(input().split())
    list_Q = []
    for i in range(Q):
        list_Q.append(input().split())
    return list_N, list_Q
