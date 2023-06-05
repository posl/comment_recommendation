def main():
    S = input()
    T = input()
    if S == T:
        print(0)
        return
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()