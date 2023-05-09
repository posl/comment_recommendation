def main():
    N, K = map(int, input().split())
    # お菓子を持っている人数をカウントする
    # お菓子を持っていない場合は0
    # お菓子を持っている場合は1
    # すべての人が持っている場合はK
    cnt = [0] * N
    for _ in range(K):
        d = int(input())
        for a in map(int, input().split()):
            cnt[a - 1] += 1
    # 0の人数をカウント
    print(cnt.count(0))

if __name__ == '__main__':
    main()