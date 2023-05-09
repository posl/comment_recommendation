def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    ans = 0
    for i in range(N):
        if S[i] in S[:i]:
            continue
        if T[i] > T[ans]:
            ans = i
    print(ans + 1)
