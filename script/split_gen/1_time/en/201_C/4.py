def main():
    S = input()
    if S[0] == 'o':
        ans = 9
    else:
        ans = 10
    for i in range(1, 10):
        if S[i] == 'o':
            ans *= 9 - i
        elif S[i] == '?':
            ans *= 10 - i
    print(ans)
