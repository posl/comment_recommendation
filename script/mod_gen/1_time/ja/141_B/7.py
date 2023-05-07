def main():
    S = input()
    for i in range(len(S)):
        if (i+1)%2 == 1:
            if S[i] == "R":
                continue
            else:
                print("No")
                exit()
        else:
            if S[i] == "L":
                continue
            else:
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()