def main():
    S = input()
    n = len(S)
    ans = 0
    for i in range(n):
        ans += (ord(S[i])-64)*pow(26, n-i-1)
    print(ans)
