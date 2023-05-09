def main():
    n = int(input())
    s = [input() for i in range(n)]
    cnt = {}
    for i in range(n):
        if s[i] not in cnt:
            cnt[s[i]] = 0
            print(s[i])
        else:
            cnt[s[i]] += 1
            print(s[i] + '(' + str(cnt[s[i]]) + ')')
