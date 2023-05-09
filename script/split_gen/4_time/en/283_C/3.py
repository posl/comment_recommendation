def main():
    S = input()
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            ans += 1
        else:
            ans += int(S[i])
            if i != len(S) - 1:
                ans += 1
    print(ans)
