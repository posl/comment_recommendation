Synthesizing 10/10 solutions

=======
Suggestion 1

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
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        sum = sum - (A[B[i]-1]*B.count(B[i])) + (C[i]*B.count(B[i]))
        print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    s = sum(a)
    for b, c in bc:
        s += (c - b) * a.count(b)
        print(s)
        a = [c if x == b else x for x in a]

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b1, c1 = map(int, input().split())
        b.append(b1)
        c.append(c1)
    a_sum = sum(a)
    b_sum = {}
    for i in range(n):
        if a[i] in b_sum:
            b_sum[a[i]] += 1
        else:
            b_sum[a[i]] = 1
    for i in range(q):
        if b[i] in b_sum:
            a_sum += (c[i] - b[i]) * b_sum[b[i]]
            if c[i] in b_sum:
                b_sum[c[i]] += b_sum[b[i]]
            else:
                b_sum[c[i]] = b_sum[b[i]]
            b_sum[b[i]] = 0
        print(a_sum)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    sumA = sum(A)
    cnt = [0] * 100001
    for a in A:
        cnt[a] += 1

    for b, c in BC:
        sumA += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(sumA)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    A_sum = sum(A)
    B_sum = [0] * (10**5 + 1)
    for i in range(N):
        B_sum[A[i]] += 1

    for i in range(Q):
        A_sum += (BC[i][1] - BC[i][0]) * B_sum[BC[i][0]]
        B_sum[BC[i][1]] += B_sum[BC[i][0]]
        B_sum[BC[i][0]] = 0
        print(A_sum)

=======
Suggestion 6

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
    for b, c in bc:
        if b in d:
            s += (c-b)*d[b]
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            d[b] = 0
        print(s)

=======
Suggestion 7

def main():
    # read input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = []
    for i in range(Q):
        BC.append(list(map(int, input().split())))

    # calculate
    A_sum = sum(A)
    A_count = [0] * (10**5 + 1)
    for i in range(N):
        A_count[A[i]] += 1
    for i in range(Q):
        A_sum += (BC[i][1] - BC[i][0]) * A_count[BC[i][0]]
        A_count[BC[i][1]] += A_count[BC[i][0]]
        A_count[BC[i][0]] = 0
        print(A_sum)

=======
Suggestion 8

def problem171_d():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    
    sum_A = sum(A)
    count = {}
    for i in A:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for i in range(Q):
        sum_A -= count[BC[i][0]] * BC[i][0]
        sum_A += count[BC[i][0]] * BC[i][1]
        if BC[i][1] in count:
            count[BC[i][1]] += count[BC[i][0]]
        else:
            count[BC[i][1]] = count[BC[i][0]]
        count[BC[i][0]] = 0
        print(sum_A)

=======
Suggestion 9

def main():
    # Get the number of elements in the sequence
    num_elems = int(input())
    # Get the sequence
    seq = input().split()
    # Get the number of operations
    num_ops = int(input())
    # Get the operations
    ops = []
    for i in range(num_ops):
        ops.append(input().split())
    # For each operation, replace the elements in the sequence
    for i in range(num_ops):
        for j in range(num_elems):
            if seq[j] == ops[i][0]:
                seq[j] = ops[i][1]
    # Print the sum of the elements in the sequence
    print(sum(map(int, seq)))

=======
Suggestion 10

def main():
    print('Start')
    print('Enter number of elements in list')
    n = int(input())
    print('Enter the elements of the list')
    a = list(map(int,input().split()))
    print('Enter number of operations')
    q = int(input())
    print('Enter the elements of the list')
    b = []
    c = []
    for i in range(q):
        b.append(int(input()))
        c.append(int(input()))
    print('The list of sums after each operation is:')
    for i in range(q):
        a = [c[i] if j==b[i] else j for j in a]
        print(sum(a))
    print('End')
