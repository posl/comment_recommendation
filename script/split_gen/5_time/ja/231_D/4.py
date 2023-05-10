def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
