def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif S[i] != S[i-1]:
            ans += 1
    print(ans)
