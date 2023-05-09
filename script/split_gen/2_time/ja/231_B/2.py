def main():
    N = int(input())
    S = [input() for _ in range(N)]
    max = 0
    for i in range(N):
        if S.count(S[i]) > max:
            max = S.count(S[i])
            name = S[i]
    print(name)
