def main():
    S = input()
    S = list(S)
    S.sort()
    S = "".join(S)
    S = S.replace(" ", "")
    S = S.replace("\n", "")
    print(S)
    if S == "abc":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()