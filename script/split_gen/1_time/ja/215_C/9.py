def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = ''.join(S)
    print(S)
    print(K)
    print(S[K-1])
