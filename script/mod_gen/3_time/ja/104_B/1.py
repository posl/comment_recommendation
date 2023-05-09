def main():
    S = input()
    if S[0] == "A":
        if S[2:-1].count("C") == 1:
            if S.replace("A","").replace("C","").islower():
                print("AC")
                exit()
    print("WA")

if __name__ == '__main__':
    main()