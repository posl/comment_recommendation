def main():
    S = input()
    if (S[::2].count("U") + S[::2].count("D") == len(S[::2])) and (S[1::2].count("L") + S[1::2].count("R") == len(S[1::2])):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()