def main():
    S = input()
    if len(S) == 1:
        if S == "8":
            print("Yes")
        else:
            print("No")
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(112, 1000, 8):
            if len(set(str(i))) == 3 and set(str(i)).issubset(set(S)):
                print("Yes")
                break
        else:
            print("No")

if __name__ == '__main__':
    main()