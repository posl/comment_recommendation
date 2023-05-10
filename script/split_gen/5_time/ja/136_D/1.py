def main():
    s = input()
    l = len(s)
    ans = [0 for i in range(l)]
    cnt = 0
    flag = False
    for i in range(l):
        if s[i] == 'R':
            cnt += 1
            flag = False
        else:
            if flag:
                cnt += 1
            else:
                ans[i] += cnt//2
                ans[i-1] += cnt//2
                if cnt % 2 == 1:
                    ans[i-1] += 1
                    flag = True
                cnt = 0
    cnt = 0
    flag = False
    for i in range(l-1, -1, -1):
        if s[i] == 'L':
            cnt += 1
            flag = False
        else:
            if flag:
                cnt += 1
            else:
                ans[i] += cnt//2
                ans[i+1] += cnt//2
                if cnt % 2 == 1:
                    ans[i+1] += 1
                    flag = True
                cnt = 0
    print(*ans)
