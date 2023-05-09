def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    for i in range(1, 10):
        if S[i] == "1":
            continue
        if S[i-1] == "1":
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()