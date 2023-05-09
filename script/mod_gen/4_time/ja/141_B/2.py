def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == "L":
            print("No")
            return
        elif i % 2 == 1 and S[i] == "R":
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()