def main():
    S = input()
    N = len(S)
    for i in range(N):
        if S[i] != S[N - 1 - i]:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()