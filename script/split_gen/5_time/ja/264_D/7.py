def main():
    s = input()
    s = list(s)
    atcoder = list('atcoder')
    cnt = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            cnt += 1
    print(cnt)
