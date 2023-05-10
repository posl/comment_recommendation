def main():
    S = input()
    n = len(S)
    ans = 0
    for i in range(0,n-3):
        for j in range(i+3,n+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)
