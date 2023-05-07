def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    maxT = max(T)
    for i in range(N):
        if T[i] == maxT:
            if S[i] not in S[:i]:
                print(i+1)
                break
