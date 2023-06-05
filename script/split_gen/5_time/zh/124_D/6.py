def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    cnt = 0
    if S[0] == '0':
        cnt += 1
    for i in range(N-1):
        if S[i] == '1' and S[i+1] == '0':
            cnt += 1
    if S[-1] == '0':
        cnt += 1
    print(min(cnt+2*K, N)-1)
