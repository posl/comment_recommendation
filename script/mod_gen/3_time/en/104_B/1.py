def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    if S[1:].replace("C", "").islower() == False:
        print("WA")
        return
    print("AC")
    return

if __name__ == '__main__':
    main()