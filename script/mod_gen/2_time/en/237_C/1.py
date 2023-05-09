def main():
    S = input()
    N = len(S)
    for i in range(N):
        if S[i] != S[N-1-i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()