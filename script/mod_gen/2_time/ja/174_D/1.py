def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "R":
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()