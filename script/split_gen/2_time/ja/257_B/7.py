def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    pos = [0] * (N+1)
    for i in range(K):
        pos[A[i]] = i+1
    for i in L:
        if pos.index(i) == N:
            continue
        elif pos[pos.index(i)+1] == 0:
            pos[pos.index(i)] = 0
            pos[pos.index(i)+1] = i
        else:
            continue
    for i in range(1, N+1):
        if pos[i] == 0:
            print(i, end=' ')
        else:
            print(pos.index(pos[i]), end=' ')
