def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(N):
            if i != j:
                if S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]:
                    print("No")
                    return
    print("Yes")
    return
