def main():
    S = input()
    N = len(S)
    ans = [0 for i in range(N)]
    R = 0
    L = 0
    flag = 0
    for i in range(N):
        if S[i] == "R":
            if flag == 1:
                ans[i-1] = R//2 + L//2 + R%2
                ans[i] = R//2 + L//2 + L%2
                R = 0
                L = 0
                flag = 0
            R += 1
        else:
            L += 1
            flag = 1
    ans[N-1] = R//2 + L//2 + R%2
    ans[0] = R//2 + L//2 + L%2
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()