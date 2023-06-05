def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    for i in S[1:]:
        if i != "C" and i.isupper():
            print("WA")
            return
    print("AC")

if __name__ == '__main__':
    main()