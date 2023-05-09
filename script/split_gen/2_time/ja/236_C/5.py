def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    S = set(S)
    T = set(T)
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')
