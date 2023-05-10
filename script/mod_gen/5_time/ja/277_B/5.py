def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()