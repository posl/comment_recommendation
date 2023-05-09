def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    T.sort(reverse=True)
    print(S[T.index(T[1])])
