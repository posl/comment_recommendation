def main():
    s = input()
    res = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 0
    print(res)
