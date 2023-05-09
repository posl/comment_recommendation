def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    elif len(S) < len(T):
        if S[-1] == T[-1]:
            main()
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()