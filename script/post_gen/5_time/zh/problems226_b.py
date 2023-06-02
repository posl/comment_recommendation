Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    # print(L)
    L.sort()
    # print(L)
    cnt = 1
    for i in range(1, N):
        if L[i] != L[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(input().split())
    l = list(map(lambda x: x[1:], l))
    l = list(map(lambda x: ''.join(x), l))
    print(len(set(l)))

=======
Suggestion 3

def main():
    n = int(input())
    seqs = []
    for i in range(n):
        seqs.append(list(map(int,input().split()))[1:])
    seqs.sort()
    ans = 1
    for i in range(1,n):
        if seqs[i] != seqs[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    d = {}
    for i in range(N):
        L = list(map(int, input().split(" ")))
        L = L[1:]
        L = tuple(L)
        if L not in d:
            d[L] = 1
        else:
            d[L] += 1
    print(len(d))

=======
Suggestion 5

def main():
    N = int(input())
    seqs = []
    for i in range(N):
        seqs.append(list(map(int, input().split()[1:])))
    seqs.sort()
    # print(seqs)
    ans = 1
    for i in range(N-1):
        if seqs[i] != seqs[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = list(map(int, input().split()))
        s.add(tuple(l[1:]))
    print(len(s))

=======
Suggestion 7

def main():
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split(" "))))
    lst.sort()
    count = 1
    for i in range(1, N):
        if lst[i] != lst[i-1]:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    import sys
    N = int(sys.stdin.readline().strip())
    seqs = []
    for i in range(N):
        seq = sys.stdin.readline().strip().split()
        seqs.append(seq[1:])
    print(len(set(tuple(seq) for seq in seqs)))

=======
Suggestion 9

def main():
    n = int(input())
    d = {}
    for _ in range(n):
        l = list(map(int, input().split()))
        if len(l) > 1:
            l.pop(0)
        s = ''.join(map(str, l))
        d[s] = 1
    print(len(d))

=======
Suggestion 10

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    #print(L)
    #print(len(L))
    #print(len(L[0]))
    #print(int(L[0][1]))
    #print(L[0][1])
    #print(L[0][2])
    #print(type(L[0][2]))
    #print(int(L[0][2]))
    #print(type(int(L[0][2])))
    #print(L[0][2] == L[0][2])
    #print(L[0][1] == L[1][1])
    #print(L[0][2] == L[1][2])
    #print(L[0][1] == L[1][1] and L[0][2] == L[1][2])
    #print(L[0][1] == L[1][1] and L[0][2] == L[1][2] and L[0][3] == L[1][3])
    #print(L[0][1] == L[1][1] and L[0][2] == L[1][2] and L[0][3] == L[1][3] and L[0][4] == L[1][4])
    #print(L[0][1] == L[1][1] and L[0][2] == L[1][2] and L[0][3] == L[1][3] and L[0][4] == L[1][4] and L[0][5] == L[1][5])
    #print(L[0][1] == L[1][1] and L[0][2] == L[1][2] and L[0][3] == L[1][3] and L[0][4] == L[1][4] and L[0][5] == L[1][5] and L[0][6] == L[1][6])
    #print(L[0][1] == L[1][1] and L[0][2] == L[1][2] and L[0][3] == L[1][3] and L[0][4] == L[1][4]
