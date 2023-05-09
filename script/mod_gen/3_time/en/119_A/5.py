def main():
    S = input()
    S = S.split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) > 2019:
        print("TBD")
    else:
        if int(S[1]) < 4:
            print("Heisei")
        elif int(S[1]) > 4:
            print("TBD")
        else:
            if int(S[2]) <= 30:
                print("Heisei")
            else:
                print("TBD")

if __name__ == '__main__':
    main()