def main():
    S = input()
    atcoder = 'atcoder'
    ans = 0
    for i in range(len(S)):
        if S[i] != atcoder[i]:
            ans += abs(ord(S[i]) - ord(atcoder[i]))
    print(ans)
