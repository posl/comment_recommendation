def main():
    S = input()
    if len(S) % 2 == 0:
        print("Yes" if S[0::2].count("L") == 0 and S[1::2].count("R") == 0 else "No")
    else:
        print("No")

if __name__ == '__main__':
    main()