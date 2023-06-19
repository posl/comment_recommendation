def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        S = S.replace("A","")
        S = S.replace("C","")
        if S.islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

if __name__ == '__main__':
    main()