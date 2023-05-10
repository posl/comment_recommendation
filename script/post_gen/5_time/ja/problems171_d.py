Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for i in range(Q)]
    
    total = sum(A)
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        count = A.count(B)
        total += (C-B)*count
        print(total)
        A = [C if a == B else a for a in A]

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    s = sum(A)
    for b, c in BC:
        s += (c - b) * A.count(b)
        print(s)
        A = [c if a == b else a for a in A]

=======
Suggestion 3

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    sumA = sum(A)
    cnt = [0] * (10**5+1)
    for i in range(10**5+1):
        cnt[i] = A.count(i)

    # output
    for i in range(Q):
        sumA += (BC[i][1] - BC[i][0]) * cnt[BC[i][0]]
        cnt[BC[i][1]] += cnt[BC[i][0]]
        cnt[BC[i][0]] = 0
        print(sumA)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_c = list(map(int,input().split()))
        b.append(b_c[0])
        c.append(b_c[1])

    b_set = set(b)
    b_list = list(b_set)
    b_list.sort()
    b_list.reverse()
    b_list.append(0)

    c_list = []
    for i in range(len(b_list)-1):
        c_list.append(0)

    for i in range(len(b_list)-1):
        for j in range(len(b)):
            if b_list[i] == b[j]:
                c_list[i] += c[j]
    #print(b_list)
    #print(c_list)
    #print(a)
    #print("")

    for i in range(len(a)):
        for j in range(len(b_list)-1):
            if a[i] == b_list[j]:
                a[i] = c_list[j]

    for i in range(len(a)):
        print(a[i],end=" ")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    s = sum(a)
    dic = {}
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in range(q):
        b, c = bc[i]
        if b in dic:
            s += (c - b) * dic[b]
            if c in dic:
                dic[c] += dic[b]
            else:
                dic[c] = dic[b]
            del dic[b]
        print(s)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        print(sum - A[B-1] * (A[B-1] - C) + C * (A[B-1] - C))
        A[B-1] = C
        sum = sum - A[B-1] * (A[B-1] - C) + C * (A[B-1] - C)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0]*q
    c = [0]*q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    #print(n, a, q, b, c)
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    #print(d)
    s = sum(a)
    for i in range(q):
        if b[i] in d:
            s = s - b[i]*d[b[i]] + c[i]*d[b[i]]
            if c[i] in d:
                d[c[i]] += d[b[i]]
            else:
                d[c[i]] = d[b[i]]
            d[b[i]] = 0
        print(s)

=======
Suggestion 8

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    S = sum(A)
    cnt = [0] * (10 ** 5 + 1)
    for a in A:
        cnt[a] += 1

    for b, c in BC:
        S += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(S)

    # output

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sumA = sum(A)
    cnt = [0] * 100001
    for i in range(N):
        cnt[A[i]] += 1
    for i in range(Q):
        sumA = sumA + (BC[i][1] - BC[i][0]) * cnt[BC[i][0]]
        cnt[BC[i][1]] += cnt[BC[i][0]]
        cnt[BC[i][0]] = 0
        print(sumA)

=======
Suggestion 10

def main():
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())
  b = []
  c = []
  for i in range(q):
    b_c = list(map(int, input().split()))
    b.append(b_c[0])
    c.append(b_c[1])
  for i in range(q):
    for j in range(n):
      if a[j] == b[i]:
        a[j] = c[i]
    print(sum(a))
