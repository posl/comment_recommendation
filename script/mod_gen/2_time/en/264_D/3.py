def main():
    # input
    S = input()
    # compute
    ans = 0
    for i in range(len(S)//2):
        if S[i] != S[-1-i]:
            ans += 1
    # output
    print(ans)

if __name__ == '__main__':
    main()