def main():
    S = input()
    print("Yes" if S[::2].count("R") + S[1::2].count("L") == len(S[::2]) else "No")

if __name__ == '__main__':
    main()