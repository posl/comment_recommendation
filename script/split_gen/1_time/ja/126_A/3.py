def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S[K-1] = S[K-1].lower()
    S = ''.join(S)
    print(S)
