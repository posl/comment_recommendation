def main():
    s = input()
    s = list(s)
    atcoder = list('atcoder')
    ans = 0
    for i in range(len(s)):
        if s[i] == atcoder[i]:
            continue
        else:
            for j in range(i+1, len(s)):
                if s[j] == atcoder[i]:
                    for k in range(j, i, -1):
                        s[k], s[k-1] = s[k-1], s[k]
                        ans += 1
                    break
    print(ans)
