def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(3):
        if s[i] == 'R':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)
