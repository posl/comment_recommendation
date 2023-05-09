def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # おいしい順に並び替え
    A.sort(reverse=True)
    # 嫌いな食品のおいしさを取得
    dislike = [A[b-1] for b in B]
    # おいしい順に並び替え
    dislike.sort(reverse=True)
    # 嫌いな食品の最大値とおいしい順に並び替えた食品の最大値が同じならば嫌いな食品を食べる可能性がある
    if dislike[0] == A[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()