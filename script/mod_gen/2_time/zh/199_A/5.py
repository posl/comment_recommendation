def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    n = max(len(s1), len(s2), len(s3))
    s1 += '0' * (n - len(s1))
    s2 += '0' * (n - len(s2))
    s3 += '0' * (n - len(s3))
    used = set()
    for i in range(10):
        used.add(str(i))
    def check(n1, n2, n3):
        if len(n1) != len(s1) or len(n2) != len(s2) or len(n3) != len(s3):
            return False
        if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
            return False
        d = {}
        for i in range(n):
            if n1[i] in d:
                if d[n1[i]] != s1[i]:
                    return False
            else:
                d[n1[i]] = s1[i]
                used.discard(s1[i])
            if n2[i] in d:
                if d[n2[i]] != s2[i]:
                    return False
            else:
                d[n2[i]] = s2[i]
                used.discard(s2[i])
            if n3[i] in d:
                if d[n3[i]] != s3[i]:
                    return False
            else:
                d[n3[i]] = s3[i]
                used.discard(s3[i])
        return True
    def dfs(n1, n2, n3, i):
        if i == n:
            if check(n1, n2, n3):
                print(n1[::-1])
                print(n2[::-1])
                print(n3[::-1])
                exit()
            return
        if s1[i] in d:
            if s2[i] in d:
                if d[s1[i]] == d[s2[i]]:
                    dfs(n1, n2, n3, i + 1)
                else:
                    return
            else:
                if s3[i] in d:
                    if d[s1[i]] == d[s3

if __name__ == '__main__':
    main()