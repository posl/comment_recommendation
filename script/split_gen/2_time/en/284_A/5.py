def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N - 1 - i])
