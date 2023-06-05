def main():
    P = input().split(" ")
    S = ""
    for i in range(26):
        S += chr(int(P[i]) + ord("a") - 1)
    print(S)
