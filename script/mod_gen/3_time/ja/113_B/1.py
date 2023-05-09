def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    # 宮殿を建設すべき地点の番号を出力
    print(H.index(min(H, key=lambda x: abs(A - (T - x * 0.006)))))

if __name__ == '__main__':
    main()