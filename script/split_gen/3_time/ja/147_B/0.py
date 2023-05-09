def main():
    s = input()
    l = len(s)
    cnt = 0
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            cnt += 1
    print(cnt)
