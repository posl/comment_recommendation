def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W_0 = []
    W_1 = []
    for i in range(N):
        if S[i] == '0':
            W_0.append(W[i])
        else:
            W_1.append(W[i])
    W_0.sort()
    W_1.sort()
    W_0.append(10**9+1)
    W_1.append(10**9+1)
    W_0 = W_0 + [0] * len(W_1)
    W_1 = W_1 + [0] * len(W_0)
    ans = 0
    i_0 = 0
    i_1 = 0
    for i in range(N):
        if S[i] == '0':
            if W_1[i_1] < W_0[i_0]:
                ans += 1
                i_1 += 1
            else:
                i_0 += 1
        else:
            if W_0[i_0] < W_1[i_1]:
                ans += 1
                i_0 += 1
            else:
                i_1 += 1
    print(ans)

if __name__ == '__main__':
    main()