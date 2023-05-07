def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(1,N):
        if S[i] in S[:i] or S[i-1][-1] != S[i][0]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()