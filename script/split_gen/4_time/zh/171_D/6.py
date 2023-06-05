def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    S = sum(A)
    for i in range(Q):
        B, C = BC[i]
        S += (C - B) * A.count(B)
        print(S)
        A = [C if a == B else a for a in A]
    return
main()
