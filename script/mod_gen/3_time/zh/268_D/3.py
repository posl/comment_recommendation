def getStr(s, n):
    if n == 1:
        return s[0]
    else:
        s.sort()
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(len(s[i])):
                    for l in range(len(s[j])):
                        if s[i][k:] == s[j][:len(s[i]) - k] and s[j][len(s[i]) - k:] == s[i][:k]:
                            return s[j] + s[i][k:]
        return -1

if __name__ == '__main__':
    getStr()