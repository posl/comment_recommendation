def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. p1 = (0, 0) からスタート
    # 2. p2 = (A1, 0) になるように移動
    # 3. p3 = (A1, A2) になるように移動
    # 4. p4 = (A1, A2 + A3) になるように移動
    # 5. p5 = (A1 + A4, A2 + A3) になるように移動
    # 6. p6 = (A1 + A4, A2 + A3 + A5) になるように移動
    # 7. p7 = (A1 + A4 + A6, A2 + A3 + A5) になるように移動
    # 8. p8 = (A1 + A4 + A6, A2 + A3 + A5 + A7) になるように移動
    # 9. p9 = (A1 + A4 + A6 + A8, A2 + A3 + A5 + A7) になるように移動
    # 10. p10 = (A1 + A4 + A6 + A8, A2 + A3 + A5 + A7 + A9) になるように移動
    # 11. p11 = (x, y) になるように移動
    # 12. p11 と p1 の距離が A1 であることを確認
    # 13. p1 と p2 の距離が A2 であることを確認
    # 14. p2 と p3 の距離が A3 であることを確認
    # 15. p3 と p4 の距離が A4 であることを確

if __name__ == '__main__':
    main()