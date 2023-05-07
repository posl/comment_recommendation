def main():
    S = input()
    L = len(S)
    ans = [0] * L
    R = 0
    L = 0
    for i in range(L):
        if S[i] == 'R':
            R += 1
        else:
            L += 1
            ans[i] = R // 2
            ans[i - 1] = (R + 1) // 2
            R = 0
    ans[0] = R
    ans[-1] = L
    print(*ans)

if __name__ == '__main__':
    main()