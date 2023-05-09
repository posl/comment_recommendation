def main():
    N = int(input())
    S = input()
    R = []
    G = []
    B = []
    for i in range(N):
        if S[i] == 'R':
            R.append(i)
        elif S[i] == 'G':
            G.append(i)
        else:
            B.append(i)
    ans = len(R) * len(G) * len(B)
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)
