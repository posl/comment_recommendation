def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()