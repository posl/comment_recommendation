def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if T == S[i:] + S[:i]:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()