def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L_R_X = [list(map(int, input().split())) for _ in range(Q)]
    for l, r, x in L_R_X:
        print(A[l-1:r].count(x))
