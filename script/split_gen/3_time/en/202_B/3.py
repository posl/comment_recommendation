def main():
    S = input()
    S = S[::-1]
    S = S.replace("0", "a")
    S = S.replace("1", "b")
    S = S.replace("6", "1")
    S = S.replace("8", "2")
    S = S.replace("9", "6")
    S = S.replace("a", "0")
    S = S.replace("b", "1")
    print(S)
