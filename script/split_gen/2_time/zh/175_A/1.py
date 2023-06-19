def main():
    s = input()
    cnt = 0
    max_cnt = 0
    for i in s:
        if i == 'R':
            cnt += 1
        else:
            cnt = 0
        if cnt > max_cnt:
            max_cnt = cnt
    print(max_cnt)
main()
