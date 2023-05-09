def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    if S[1:].lower() != S[1:]:
        print("WA")
        return
    if S[2:-1].replace("C", "").lower() != S[2:-1].replace("C", ""):
        print("WA")
        return
    print("AC")

if __name__ == '__main__':
    main()