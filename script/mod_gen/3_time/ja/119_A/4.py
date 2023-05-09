def main():
    #S = input()
    S = "2019/11/01"
    #print(S)
    S = S.split("/")
    #print(S)
    if int(S[1]) <= 4:
        print("Heisei")
    else:
        print("TBD")

if __name__ == '__main__':
    main()