def main():
    S = input()
    N = len(S)
    ans = [0] * N
    L = 0
    R = 0
    for i in range(N):
        if S[i] == 'L':
            L += 1
        else:
            R += 1
        if S[i] == 'R' and S[i+1] == 'L':
            ans[i] = (L+1)//2 + R//2
            ans[i+1] = L//2 + (R+1)//2
            L = 0
            R = 0
    print(*ans)

if __name__ == '__main__':
    main()