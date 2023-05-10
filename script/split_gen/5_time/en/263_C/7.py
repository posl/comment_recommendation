def main():
    N, M = map(int, input().split())
    A = []
    for i in range(1, M+1):
        A.append(i)
    import itertools
    for x in itertools.combinations(A, N):
        print(*x)
