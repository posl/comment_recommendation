def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != '0':
            ans += 1
    ans += len(S) - 1
    print(ans)
