def main():
    S = input()
    K = int(input())
    S = S.replace("2","22")
    S = S.replace("3","333")
    S = S.replace("4","4444")
    S = S.replace("5","55555")
    S = S.replace("6","666666")
    S = S.replace("7","7777777")
    S = S.replace("8","88888888")
    S = S.replace("9","999999999")
    print(S[K-1])

if __name__ == '__main__':
    main()