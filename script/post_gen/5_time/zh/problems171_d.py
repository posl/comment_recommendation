Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    a_sum = sum(a)
    cnt = {}
    for i in a:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for b, c in bc:
        if b in cnt:
            a_sum += (c - b) * cnt[b]
            if c in cnt:
                cnt[c] += cnt[b]
            else:
                cnt[c] = cnt[b]
            cnt[b] = 0
        print(a_sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]

    sum_a = sum(a)
    b = [0] * 100001
    for i in a:
        b[i] += 1

    for i in range(q):
        sum_a += (bc[i][1] - bc[i][0]) * b[bc[i][0]]
        b[bc[i][1]] += b[bc[i][0]]
        b[bc[i][0]] = 0
        print(sum_a)

=======
Suggestion 3

def replace_list(list, b, c):
    for i in range(len(list)):
        if list[i] == b:
            list[i] = c
    return list

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for i in range(q)]

for i in range(q):
    a = replace_list(a, bc[i][0], bc[i][1])
    print(sum(a))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    sum_a = sum(a)
    cnt = {}
    for i in a:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    for b, c in bc:
        if b not in cnt:
            print(sum_a)
            continue
        sum_a += (c - b) * cnt[b]
        print(sum_a)
        if c not in cnt:
            cnt[c] = cnt[b]
        else:
            cnt[c] += cnt[b]
        cnt[b] = 0

=======
Suggestion 5

def main():
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    b=[]
    c=[]
    for i in range(q):
        b1,c1=map(int,input().split())
        b.append(b1)
        c.append(c1)
    sum=0
    for i in range(n):
        sum+=a[i]
    for i in range(q):
        sum=sum+(c[i]-b[i])*a.count(b[i])
        print(sum)
        sum=sum-(c[i]-b[i])*a.count(b[i])
main()

=======
Suggestion 6

def read_data():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    return N, A, Q, BC

=======
Suggestion 7

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    # Q = int(input())
    # BC = [list(map(int, input().split())) for _ in range(Q)]
    N = 4
    A = [1, 2, 3, 4]
    Q = 3
    BC = [[1, 2], [3, 4], [2, 4]]
    for i in range(Q):
        for j in range(N):
            if A[j] == BC[i][0]:
                A[j] = BC[i][1]
        print(sum(A))
    # print(A)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A_sum = sum(A)
    for i in range(Q):
        A_sum += (C[i] - B[i]) * A.count(B[i])
        print(A_sum)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    s = sum(a)
    for i in range(q):
        b, c = map(int, input().split())
        s += (c - b) * a.count(b)
        print(s)
        a = [c if x == b else x for x in a]

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for _ in range(q):
        bc.append(list(map(int, input().split())))
    sum_a = sum(a)
    for i in range(q):
        sum_a += (bc[i][1] - bc[i][0]) * a.count(bc[i][0])
        print(sum_a)
        a = [bc[i][1] if x == bc[i][0] else x for x in a]
