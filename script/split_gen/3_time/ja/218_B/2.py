def main():
    P = input().split()
    S = ""
    for i in range(26):
        S += chr(ord('a') + int(P[i]) - 1)
    print(S)
