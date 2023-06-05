def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        cnt = 0
        while i+cnt < n:
            if s[cnt] == s[i+cnt]:
                break
            cnt += 1
        print(cnt)
