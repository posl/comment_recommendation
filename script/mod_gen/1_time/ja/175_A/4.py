def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for i in range(len(S)):
        if S[i] == 'R':
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(max_cnt)

if __name__ == '__main__':
    main()