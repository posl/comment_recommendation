def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for s in S:
        if s == 'R':
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt
    print(max_cnt)
