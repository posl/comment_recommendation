def main():
    N = int(input())
    S = [input() for i in range(N)]
    S = sorted(S)
    S = sorted(S, key=S.count, reverse=True)
    print(S[0])
