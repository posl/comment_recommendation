def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    cnt = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(min(N-1, cnt+2*K))
