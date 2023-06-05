def main():
    S = input()
    if S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
        print("1")
    elif S[0] == S[1] and S[1] != S[2]:
        print("2")
    elif S[0] != S[1] and S[1] == S[2]:
        print("3")
    else:
        print("-1")

if __name__ == '__main__':
    main()