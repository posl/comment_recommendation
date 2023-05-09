def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    A = [0] * len(S)
    B = [0] * len(S)
    C = [0] * len(S)
    for i, s in enumerate(S):
        if s == 'A':
            A[i] = 1
        elif s == 'B':
            B[i] = 1
        else:
            C[i] = 1
    for i in range(1, len(S)):
        A[i] += A[i-1]
        B[i] += B[i-1]
        C[i] += C[i-1]
    for t, k in queries:
        if t % 3 == 0:
            print(S[k-1])
        elif t % 3 == 1:
            if A[k-1] > 0:
                print('A')
            elif B[k-1] > 0:
                print('B')
            else:
                print('C')
        else:
            if A[k-1] > B[k-1]:
                print('A')
            elif B[k-1] > C[k-1]:
                print('B')
            else:
                print('C')
