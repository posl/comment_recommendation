def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            if ord(S[i]) - ord(T[i]) != -25:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()