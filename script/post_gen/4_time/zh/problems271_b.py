Synthesizing 10/10 solutions

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
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(l[s-1][t-1])

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for _ in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 4

def get_input():
    n, q = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    s = []
    for i in range(q):
        s.append(list(map(int, input().split())))
    return n, q, l, s

=======
Suggestion 5

def solve():
    n,q = list(map(int,input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(q):
        s,t = list(map(int,input().split()))
        print(arr[s-1][t-1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

main()

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(q):
        i, j = map(int, input().split())
        print(a[i-1][j-1])

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in range(q):
        s,t = map(int,input().split())
        print(a[s-1][t-1])

main()

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    #print(n, q)
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    #print(a)
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 10

def get_input():
    input_list = list(map(int, input().split()))
    N = input_list[0]
    Q = input_list[1]
    seq_list = []
    for i in range(N):
        seq_list.append(list(map(int, input().split())))
    query_list = []
    for i in range(Q):
        query_list.append(list(map(int, input().split())))
    return N, Q, seq_list, query_list
