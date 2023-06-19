def main():
    # S = input()
    S = "0601889"
    # S = "86910"
    # S = "01010"
    S = list(S)
    S.reverse()
    for i in range(len(S)):
        if S[i] == "6":
            S[i] = "9"
        elif S[i] == "9":
            S[i] = "6"
    print("".join(S))
