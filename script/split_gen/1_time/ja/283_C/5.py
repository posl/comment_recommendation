def main():
    S = input()
    if S == '0':
        print(0)
        return
    ans = 0
    for i in range(len(S)):
        if i == 0:
            if S[i] == '1':
                ans += 1
            elif S[i] == '0':
                ans += 0
            else:
                ans += 2
        else:
            if S[i] == '0':
                ans += 0
            else:
                ans += 1
    ans += len(S) - 1
    print(ans)
