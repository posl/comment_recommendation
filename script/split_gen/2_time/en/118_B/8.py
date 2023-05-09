def main():
    N, M = map(int, input().split())
    D = {}
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            if a in D:
                D[a] += 1
            else:
                D[a] = 1
    print(len([i for i in D.values() if i == N]))
