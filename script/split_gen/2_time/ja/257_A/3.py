def main():
    N, X = map(int, input().split())
    S = ''
    for i in range(1, N + 1):
        for j in range(65, 91):
            S += chr(j)
    print(S[X - 1])
