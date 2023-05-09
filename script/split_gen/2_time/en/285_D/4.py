def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) != len(set(T)):
        print('No')
        return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == T[j] and T[i] == S[j]:
                print('No')
                return
    print('Yes')
    return
