def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(N):
        if i == 0:
            continue
        if S[i-1] != S[i]:
            ans += 1
    print(ans)
