def main():
    S = input()
    S = S[::-1]
    S = S.replace("0","a").replace("1","0").replace("a","1")
    S = S.replace("6","a").replace("9","6").replace("a","9")
    print(S)
main()
