def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                cnt += 1
    print(cnt)
