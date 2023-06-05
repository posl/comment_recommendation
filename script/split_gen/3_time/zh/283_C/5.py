def main():
    S = input()
    N = len(S)
    ans = N-1
    for i in range(1,1<<N):
        tmp = 0
        for j in range(N):
            if i & (1<<j):
                tmp = tmp*10 + int(S[j])
        if tmp%3 == 0:
            ans = min(ans, bin(i).count("1")-1)
    print(ans)
