def main():
    # input
    N, K = map(int, input().split())
    S = input()
    # output
    print(S[:K-1]+S[K-1].lower()+S[K:])
