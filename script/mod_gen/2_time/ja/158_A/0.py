def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[0] == S[2]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()