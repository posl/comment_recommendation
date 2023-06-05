def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if int(s[i:j+1]) % 2019 == 0:
                cnt += 1
    print(cnt)
