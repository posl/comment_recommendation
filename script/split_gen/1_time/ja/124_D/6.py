def main():
    N,K = map(int,input().split())
    S = list(input())
    for i in range(K):
        if S[i] == "0":
            S[i] = "1"
        else:
            S[i] = "0"
        if S[i] == "0":
            S[i] = "1"
        else:
            S[i] = "0"
    print(N - S.count("0"))
