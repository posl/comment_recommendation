def main():
    N = int(input())
    S = set()
    for i in range(N):
        L = list(map(int,input().split()))
        S.add(tuple(L[1:]))
    print(len(S))
