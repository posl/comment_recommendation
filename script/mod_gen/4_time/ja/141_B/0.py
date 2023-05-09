def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "L":
                print("No")
                exit()
        else:
            if S[i] == "R":
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()