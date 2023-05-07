def main():
    S = input()
    S = S[::-1]
    S = S.replace("0","2")
    S = S.replace("1","0")
    S = S.replace("2","1")
    S = S.replace("6","9")
    S = S.replace("8","8")
    S = S.replace("9","6")
    print(S)
