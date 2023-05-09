def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    S = sorted(S)
    T = sorted(T)
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()