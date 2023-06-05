def main():
    N, K = input().split()
    S = input()
    print(S[0:int(K)-1] + S[int(K)-1].lower() + S[int(K):])
