def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    ans = min(N-1, happy + K*2)
    print(ans)
