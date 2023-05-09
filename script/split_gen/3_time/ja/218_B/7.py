def main():
    P = list(map(int, input().split()))
    #print(P)
    S = ""
    for i in range(26):
        S = S + chr(ord('a') + P[i] - 1)
    print(S)
