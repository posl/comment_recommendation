def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    ans = 0
    if R > W:
        for i in range(N):
            if i % 2 == 0 and S[i] == "W":
                ans += 1
    else:
        for i in range(N):
            if i % 2 == 1 and S[i] == "R":
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()