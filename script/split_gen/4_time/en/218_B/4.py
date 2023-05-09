def main():
    P = input().split()
    S = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(S[int(P[i])-1], end="")
    print()
