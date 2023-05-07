def main():
    N = int(input())
    D = {}
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S in D:
            D[S] = max(D[S], T)
        else:
            D[S] = T
    T = []
    for s, t in D.items():
        T.append((t, s))
    T.sort(reverse=True)
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if (T, S) == T[0]:
            print(i+1)
            break
