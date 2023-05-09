def main():
    #K
    K = int(input())
    #S
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + "...")
