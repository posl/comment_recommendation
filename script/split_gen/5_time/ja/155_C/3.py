def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    #print(s)
    cnt = 1
    max_cnt = 0
    max_str = []
    for i in range(1,n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                max_str.clear()
                max_str.append(s[i-1])
            elif cnt == max_cnt:
                max_str.append(s[i-1])
            cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_str.clear()
        max_str.append(s[n-1])
    elif cnt == max_cnt:
        max_str.append(s[n-1])
    for i in range(len(max_str)):
        print(max_str[i])
