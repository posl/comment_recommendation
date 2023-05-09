def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1 and S[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

if __name__ == '__main__':
    main()