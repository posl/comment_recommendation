def main():
    S = input()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == "6":
            S = S[:i] + "9" + S[i+1:]
        elif S[i] == "9":
            S = S[:i] + "6" + S[i+1:]
    print(S)

if __name__ == '__main__':
    main()