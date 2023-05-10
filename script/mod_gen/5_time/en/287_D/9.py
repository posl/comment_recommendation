def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S.replace("?", "a")[:i] + S[i:len(S) - (len(T) - i)].replace("?", "a") == T:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()