def main():
    S = input()
    S = sorted(S)
    if S[0] != "0":
        print("No")
        return
    if S.count("0") == len(S):
        print("Yes")
        return
    if len(S) < 3:
        print("No")
        return
    for i in range(1, len(S)):
        for j in range(i+1, len(S)):
            if (int(S[i])*10+int(S[j])) % 8 == 0:
                print("Yes")
                return
            if (int(S[i])*10+int(S[j])) % 8 == 0:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()