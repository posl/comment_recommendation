def main():
    N = int(input())
    S = list(map(int, input().split()))
    for i in range(N):
        S[i] -= 3
    S.sort()
    cnt = 0
    for i in range(N):
        if S[i] <= 0:
            continue
        cnt += 1
        for j in range(i+1, N):
            if S[j] % S[i] == 0:
                S[j] = 0
    print(cnt)
