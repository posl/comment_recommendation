def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    S.sort()
    T.sort()
    if S != T:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()