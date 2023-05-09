def main():
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            cnt += 1
    print(cnt//2)
