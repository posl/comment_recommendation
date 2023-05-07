def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    if S[-1] == "0":
        print("No")
        return
    for i in range(1, 10):
        if S[i] == "1":
            if S[i-1] == "0" and S[i+1] == "0":
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()