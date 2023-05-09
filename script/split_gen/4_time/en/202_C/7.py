def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A = [a-1 for a in A]
    B = [b-1 for b in B]
    C = [c-1 for c in C]
    count = [0] * N
    for c in C:
        count[B[c]] += 1
    print(sum([count[a] for a in A]))
