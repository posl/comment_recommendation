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
    for i in range(Q):
        A = [c if a == b else a for a, b, c in zip(A, [B[i]] * N, [C[i]] * N)]
        print(sum(A))
