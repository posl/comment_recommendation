def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    h = [i for i in range(H) if '#' in A[i]]
    w = [j for j in range(W) if '#' in [A[i][j] for i in range(H)]]
    for i in h:
        print(''.join(A[i][j] for j in w))
