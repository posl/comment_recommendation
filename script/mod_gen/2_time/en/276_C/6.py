def main():
    N = int(input())
    P = list(map(int, input().split()))
    # Pの逆順
    P_rev = P[::-1]
    # Pの逆順の隣接要素の差
    d = [P_rev[i] - P_rev[i + 1] for i in range(N - 1)]
    # Pの逆順の隣接要素の差が0以上の最大のインデックス
    idx = d.index(max([x for x in d if x >= 0])) + 1
    # Pの逆順の隣接要素の差が0以上の最大のインデックス以降の要素を降順にソート
    P_rev[idx:] = sorted(P_rev[idx:], reverse=True)
    # Pの逆順を降順にソート
    P_rev = sorted(P_rev, reverse=True)
    # Pの逆順の隣接要素の差が0以上の最大のインデックス以降の要素を昇順にソート
    P_rev[idx:] = sorted(P_rev[idx:])
    # Pの逆順を昇順にソート
    P_rev = sorted(P_rev)
    # Pの逆順からPを求める
    P = P_rev[::-1]
    print(" ".join(map(str, P)))

if __name__ == '__main__':
    main()