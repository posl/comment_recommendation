def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for s in S:
        if s == 'R':
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 0
    print(max_cnt)
