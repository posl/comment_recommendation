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
    A.sort()
    for i in range(Q):
        if B[i] in A:
            A = [C[i] if x == B[i] else x for x in A]
            A.sort()
        print(sum(A))
