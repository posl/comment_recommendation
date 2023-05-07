def main():
    N, K = map(int, input().split())
    S = input()
    if K == 1:
        print(S[0].lower() + S[1:])
    else:
        print(S[:K-1] + S[K-1].lower() + S[K:])
