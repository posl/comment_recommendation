def main():
    s = input()
    k = int(input())
    l = len(s)
    cnt = 0
    for i in range(l-1):
        if s[i] == s[i+1]:
            cnt += 1
    ans = min(cnt + 2*k, l-1)
    print(ans)
