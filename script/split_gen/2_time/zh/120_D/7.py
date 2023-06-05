def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        if s[i] == "1":
            cnt += 1
    print(min(cnt, n - cnt) * 2)
