def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    express = []
    for t in T:
        for i in range(N):
            if t == S[i]:
                express.append(i)
    for i in range(N):
        if i in express:
            print('Yes')
        else:
            print('No')
