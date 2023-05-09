def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for i in range(3):
        if S[i] == "R":
            cnt += 1
        else:
            cnt = 0
        if cnt > max_cnt:
            max_cnt = cnt
    print(max_cnt)

if __name__ == '__main__':
    main()