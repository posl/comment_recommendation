def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        for i in range(1, len(S)):
            if S[i] == "C":
                continue
            elif S[i].islower():
                continue
            else:
                print("WA")
                return
        print("AC")
    else:
        print("WA")

if __name__ == '__main__':
    main()