def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if S[i+1] == 'L':
                if (i+1) % 2 == 0:
                    ans[i] += 1
                else:
                    ans[i+1] += 1
            else:
                if (i+1) % 2 == 0:
                    ans[i] += 1
                else:
                    ans[i+1] += 1
    print(*ans)

if __name__ == '__main__':
    main()