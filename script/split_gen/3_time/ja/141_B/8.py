def main():
    S = input()
    if len(S)%2 == 1:
        print("No")
    else:
        if S[0::2].count("R") + S[0::2].count("U") + S[0::2].count("D") == len(S[0::2]) and S[1::2].count("L") + S[1::2].count("U") + S[1::2].count("D") == len(S[1::2]):
            print("Yes")
        else:
            print("No")
