def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    S = [x for _, x in sorted(zip(T, S), reverse=True)]
    print(S[1])
