def main():
    S = input()
    K = int(input())
    N = len(S)
    if N >= K:
        print(S[K-1])
        return
    else:
        K -= N
        for i in range(N):
            if S[i] == '1':
                continue
            else:
                print(S[i])
                return
        print(S[-1])

if __name__ == '__main__':
    main()