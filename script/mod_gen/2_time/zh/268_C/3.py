def main():
    S = input()
    T = input()
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()