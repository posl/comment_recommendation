def main():
    S = input()
    N = len(S)
    ans = 10**N
    for i in range(2**(N-1)):
        tmp = 0
        for j in range(N):
            if i & (1<<j):
                tmp += int(S[j:])
                break
            else:
                tmp += int(S[j]) * 10**(N-j-1)
        ans = min(ans, tmp)
    print(ans)
