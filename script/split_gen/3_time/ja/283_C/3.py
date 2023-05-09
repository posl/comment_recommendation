def main():
    S = input()
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += int(S[i])
        else:
            if int(S[i]) == 0:
                ans += 1
            else:
                ans += int(S[i]) + 1
    print(ans)
