def main():
    S = input()
    l = len(S)
    ans = 0
    for i in range(l):
        for j in range(i+3, l+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)
