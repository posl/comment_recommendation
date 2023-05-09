def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            pass
        else:
            ans += 1
    if S[0] != '1':
        ans += len(S) - 1
    else:
        ans += len(S) - 2
    print(ans)
