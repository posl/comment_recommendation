def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1]+a)
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, S[i+M]-S[i])
    print(ans)
