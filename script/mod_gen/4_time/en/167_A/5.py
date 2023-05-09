def main():
    S = input()
    T = input()
    if len(S) == (len(T) - 1):
        if S == T[0:len(S)]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()