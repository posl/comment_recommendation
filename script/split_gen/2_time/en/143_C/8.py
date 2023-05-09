def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    cnt = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            cnt += 1
    print(cnt)
