def main():
    S = input()
    S = S.replace("1","1 ")
    S = S.replace("0","0 ")
    S = S.split()
    S = S[0:-1]
    S = " ".join(S)
    print(S)

if __name__ == '__main__':
    main()