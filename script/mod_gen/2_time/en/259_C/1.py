def main():
    S = input()
    T = input()
    if len(S) >= len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    if S[-1] != T[len(S)]:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()