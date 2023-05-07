def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        tmp = input().split()
        S.append(tmp[0])
        T.append(tmp[1])
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == T[j]:
                print('No')
                return
    print('Yes')
