def main():
    S = input()
    print("Yes" if S[1:9].count("1") >= 2 and S[0] == "0" and S[9] == "0" else "No")

if __name__ == '__main__':
    main()