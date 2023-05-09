def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(N):
            if i != j:
                if S[i] == S[j] and T[i] == T[j]:
                    print('Yes')
                    return
    print('No')
    return
