def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i] and j-i != k-j:
                    ans += 1
    print(ans)
