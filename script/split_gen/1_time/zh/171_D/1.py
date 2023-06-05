def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    sum = 0
    for a in A:
        sum += a
    for bc in BC:
        b = bc[0]
        c = bc[1]
        sum += (c - b) * A.count(b)
        print(sum)
        for i in range(len(A)):
            if A[i] == b:
                A[i] = c
