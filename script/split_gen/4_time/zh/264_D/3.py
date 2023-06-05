def main():
    S = input()
    atcoder = 'atcoder'
    ans = 0
    for i in range(len(S)):
        if S[i] == atcoder[i]:
            continue
        elif S[i] == 'a':
            ans += 1
        elif S[i] == 't':
            ans += 1
        elif S[i] == 'c':
            ans += 1
        elif S[i] == 'o':
            ans += 1
        elif S[i] == 'd':
            ans += 1
        elif S[i] == 'e':
            ans += 1
        elif S[i] == 'r':
            ans += 1
        else:
            ans += 2
    print(ans)
