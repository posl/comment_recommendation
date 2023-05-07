def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += len(S) - 1
        else:
            ans += 1
        if S[i] != '0':
            ans += 1
    print(ans)
