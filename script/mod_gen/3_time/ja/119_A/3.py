def main():
    S = input()
    S = S.split("/")
    if int(S[1]) <= 4:
        print("Heisei")
    else:
        print("TBD")

if __name__ == '__main__':
    main()