def main():
    S = input()
    #S = "FREE"
    #S = "FFEE"
    #S = "STOP"
    #S = "ASSA"
    S = list(S)
    S.sort()
    S = "".join(S)
    if S == "AASS" or S == "EEFF":
        print("Yes")
    else:
        print("No")
