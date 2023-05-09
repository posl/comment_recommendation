def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if M == 0:
        print('Yes')
        return
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('Yes')
    else:
        print('No')
