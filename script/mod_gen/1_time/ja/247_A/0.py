def main():
    S = input()
    for i in range(3):
        if S[i] == "1":
            S = S[:i] + "0" + S[i+1:]
        else:
            S = S[:i] + "0" + S[i+1:]
    print(S)

if __name__ == '__main__':
    main()