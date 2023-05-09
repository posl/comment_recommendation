def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            if S.count(S[i]) != T.count(T[i]):
                print("No")
                return
    print("Yes")
main()

if __name__ == '__main__':
    main()