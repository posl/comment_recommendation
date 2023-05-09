def main():
    N, L = map(int, input().split())
    # L から L+N-1 までの和を求める
    total = sum([L+i-1 for i in range(1, N+1)])
    # 食べるリンゴを決める
    if L >= 0:
        # L が 0 以上の場合、最小値は L である
        eat = L
    elif L+N-1 <= 0:
        # L+N-1 が 0 以下の場合、最小値は L+N-1 である
        eat = L+N-1
    else:
        # L 以上 L+N-1 以下の場合、最小値は 0 である
        eat = 0
    # 食べるリンゴを除いた和を求める
    print(total - eat)

if __name__ == '__main__':
    main()