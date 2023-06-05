def main():
    S = input()
    T = input()
    if (len(S) == 1 and len(T) == 2):
        print("Yes")
    elif (len(S) == 1 and len(T) == 1):
        print("No")
    elif (len(S) == len(T) - 1):
        if (S == T[0:-1]):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()