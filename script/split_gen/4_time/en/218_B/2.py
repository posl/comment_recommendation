def main():
    P = input().split()
    P = [int(i) for i in P]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    S = ""
    for i in range(26):
        S += alphabet[P[i]-1]
    print(S)
