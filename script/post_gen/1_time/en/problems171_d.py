Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    S = sum(A)
    count = [0] * (10 ** 5 + 1)
    for a in A:
        count[a] += 1
    for i in range(Q):
        count[B[i]] -= 1
        count[C[i]] += 1
        S += (C[i] - B[i]) * count[B[i]]
        print(S)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    S = sum(A)
    for i in range(Q):
        S += (C[i] - B[i]) * A.count(B[i])
        print(S)

=======
Suggestion 3

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
    ans = sum(A)
    for i in range(Q):
        ans += (C[i] - B[i]) * A.count(B[i])
        print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    
    sum_A = sum(A)
    count_B = [0]*10**5
    for i in range(N):
        count_B[A[i]-1] += 1
    for i in range(Q):
        sum_A += (C[i] - B[i]) * count_B[B[i]-1]
        count_B[C[i]-1] += count_B[B[i]-1]
        count_B[B[i]-1] = 0
        print(sum_A)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = [int(x) for x in input().split()]
    S = 0
    for i in range(N):
        S += A[i]
    for i in range(Q):
        S -= B[i] * A.count(B[i])
        S += C[i] * A.count(B[i])
        print(S)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = [int(j) for j in input().split()]
    S = sum(A)
    for i in range(Q):
        S += (C[i] - B[i]) * A.count(B[i])
        print(S)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    #print(B)
    for i in range(Q):
        C.append(B[i][1])
    #print(C)
    sum_A = sum(A)
    #print(sum_A)
    for i in range(Q):
        if B[i][0] in A:
            sum_A = sum_A - B[i][0] * A.count(B[i][0]) + C[i] * A.count(B[i][0])
        print(sum_A)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    for i in range(Q):
        C.append(B[i][1])
        B[i] = B[i][0]
    sumA = sum(A)
    for i in range(Q):
        sumA += (C[i] - B[i]) * A.count(B[i])
        print(sumA)

=======
Suggestion 9

def main():
    #read
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    
    #solve
    ans = [0] * Q
    dic = {}
    for i in range(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    total = sum(A)
    for i in range(Q):
        if B[i] in dic:
            total += (C[i] - B[i]) * dic[B[i]]
            if C[i] in dic:
                dic[C[i]] += dic[B[i]]
            else:
                dic[C[i]] = dic[B[i]]
            del dic[B[i]]
        ans[i] = total
    
    #print
    for i in range(Q):
        print(ans[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = []
    for _ in range(Q):
        BC.append(list(map(int,input().split())))
    B = [x[0] for x in BC]
    C = [x[1] for x in BC]
    S = sum(A)
    for i in range(N):
        if A[i] in B:
            S += C[B.index(A[i])]-A[i]
        print(S)
