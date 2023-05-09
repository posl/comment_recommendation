def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    X = ''.join(S)
    for i in range(3, 17):
        for j in range(0, N):
            for k in range(0, N):
                if j == k: continue
                if X == ''.join(S[j:j+1] + ['_'] * i + S[k:k+1]):
                    if X not in T:
                        print(X)
                        return
    print('-1')
