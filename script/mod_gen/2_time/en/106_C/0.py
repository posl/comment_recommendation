def main():
    S = input()
    K = int(input())
    S = S.replace("1", "a")
    S = S.replace("2", "b")
    S = S.replace("3", "c")
    S = S.replace("4", "d")
    S = S.replace("5", "e")
    S = S.replace("6", "f")
    S = S.replace("7", "g")
    S = S.replace("8", "h")
    S = S.replace("9", "i")
    print(S[K-1])

if __name__ == '__main__':
    main()