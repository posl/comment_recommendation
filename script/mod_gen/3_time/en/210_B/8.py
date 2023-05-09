def main():
    # read input
    N = int(input())
    S = input()
    # solve problem
    ans = "Aoki"
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                ans = "Takahashi"
            break
    # print answer
    print(ans)

if __name__ == '__main__':
    main()