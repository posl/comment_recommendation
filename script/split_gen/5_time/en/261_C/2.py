def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
        if d[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + '(' + str(d[S[i]]) + ')')
