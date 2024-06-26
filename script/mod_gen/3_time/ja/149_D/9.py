def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                ans += P
            elif T[i] == "s":
                ans += R
            else:
                ans += S
        else:
            if T[i] == "r":
                if T[i-K] == "r":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    ans += P
            elif T[i] == "s":
                if T[i-K] == "s":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    ans += R
            else:
                if T[i-K] == "p":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    ans += S
    print(ans)

if __name__ == '__main__':
    main()