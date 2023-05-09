def main():
    P = list(map(int, input().split()))
    S = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(P)):
        S[P[i] - 1] = chr(i + 97)
    print("".join(S))
