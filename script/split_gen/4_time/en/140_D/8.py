def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    happy = 0
    for n in range(1, N):
        if S[n-1] == S[n]:
            happy += 1
    print(min(N-1, happy+2*K))
