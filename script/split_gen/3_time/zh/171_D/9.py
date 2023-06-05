def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for a in A:
        sum += a
    for bc in BC:
        sum += (bc[1] - bc[0]) * A.count(bc[0])
        print(sum)
        sum += (bc[0] - bc[1]) * A.count(bc[0])
        for i in range(N):
            if A[i] == bc[0]:
                A[i] = bc[1]
