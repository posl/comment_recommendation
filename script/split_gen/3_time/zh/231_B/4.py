def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    M = max(S, key=S.count)
    print(M)
