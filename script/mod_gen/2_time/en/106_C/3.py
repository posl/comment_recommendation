def main():
    S = input()
    K = int(input())
    N = len(S)
    for i in range(N):
        if S[i] != "1":
            if K <= i:
                print(1)
            else:
                print(S[i])
            exit()
    print(1)

if __name__ == '__main__':
    main()