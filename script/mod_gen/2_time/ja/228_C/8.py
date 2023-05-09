def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    # 3日目までの合計点
    score = [sum(p[i]) for i in range(n)]
    # 4日目の試験の点数の上位k人の合計点
    score.sort(reverse=True)
    top = sum(score[:k])
    for i in range(n):
        # 4日目の試験で最大の合計点を取れる場合
        if score[k-1] + p[i][3] >= top:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()