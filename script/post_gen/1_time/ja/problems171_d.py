Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sumA = sum(A)
    for i in range(Q):
        sumA += BC[i][1] * (A.count(BC[i][0]) - A.count(BC[i][1]))
        print(sumA)
        A = list(map(lambda x: BC[i][1] if x == BC[i][0] else x, A))

=======
Suggestion 2

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
    a_sum = sum(a)
    for i in range(q):
        a_sum += (c[i] - b[i]) * a.count(b[i])
        print(a_sum)
        a_sum -= (c[i] - b[i]) * a.count(b[i])
        a = [c[i] if x == b[i] else x for x in a]

=======
Suggestion 3

def main():
    # input
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    BC = [list(map(int, input().split())) for _ in range(q)]

    # compute
    sumA = sum(A)
    cntA = [0] * 100001
    for a in A:
        cntA[a] += 1

    # output
    for b, c in BC:
        sumA += (c-b) * cntA[b]
        cntA[c] += cntA[b]
        cntA[b] = 0
        print(sumA)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]

    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    s = sum(a)
    for i in range(q):
        b, c = bc[i]
        if b in d:
            s += d[b] * (c - b)
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            d[b] = 0
        print(s)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, BC)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    for i in range(Q):
        sum = sum - A[BC[i][0]-1] * BC[i][1] + BC[i][1] * BC[i][0]
        A[BC[i][0]-1] = BC[i][1]
        print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    
    sum_A = sum(A)
    A_dict = {i: A.count(i) for i in set(A)}
    
    for bc in BC:
        b, c = bc[0], bc[1]
        if b in A_dict:
            sum_A += (c - b) * A_dict[b]
            if c in A_dict:
                A_dict[c] += A_dict[b]
            else:
                A_dict[c] = A_dict[b]
            A_dict[b] = 0
        print(sum_A)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    #print(N)
    #print(A)
    #print(Q)
    #print(BC)

    sum_A = sum(A)
    #print(sum_A)

    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        #print(B)
        #print(C)
        #print(A)
        #print(sum_A)

        sum_A = sum_A - B * A.count(B) + C * A.count(B)
        print(sum_A)

        A = [C if a == B else a for a in A]
        #print(A)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    cnt = [0] * 100001
    sum_a = sum(a)
    for i in range(n):
        cnt[a[i]] += 1
    for i in range(q):
        sum_a += (bc[i][1] - bc[i][0]) * cnt[bc[i][0]]
        cnt[bc[i][1]] += cnt[bc[i][0]]
        cnt[bc[i][0]] = 0
        print(sum_a)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    sum = 0
    for i in range(N):
        sum += A[i]

    for i in range(Q):
        B, C = map(int, input().split())
        sum += (C - B) * A.count(B)
        print(sum)
        A = list(map(lambda x: C if x == B else x, A))

main()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    # 1 <= N, Q <= 10^5
    # 1 <= A_i, B_i, C_i <= 10^5
    # B_i != C_i
    # 1 <= i <= Q

    S = sum(A)
