def main():
    s = input()
    atcoder = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] == atcoder[i]:
            continue
        else:
            ans += 1
    print(ans)
