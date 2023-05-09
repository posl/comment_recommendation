def main():
    S = "abcdefghijklmnopqrstuvwxyz"
    P = list(map(int, input().split()))
    ans = ""
    for i in range(26):
        ans += S[P[i]-1]
    print(ans)
