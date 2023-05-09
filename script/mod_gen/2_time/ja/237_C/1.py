def main():
    S = input()
    N = len(S)
    for i in range(N):
        if S[i] != S[N - i - 1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()