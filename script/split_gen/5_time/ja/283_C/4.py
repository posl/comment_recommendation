def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            continue
        ans += int(S[i])
        ans += 10 ** (len(S) - i - 1) - 1
    print(ans)
    return
