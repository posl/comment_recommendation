def main():
    N = int(input())
    S = input()
    ans = 0
    prev = ''
    for i in range(N):
        if prev != S[i]:
            ans += 1
        prev = S[i]
    print(ans)
