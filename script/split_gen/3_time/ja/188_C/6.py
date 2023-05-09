def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)
    # 2^N
    N2 = 2 ** N
    # print(N2)
    # 最後の対戦の勝者
    winner = 0
    # 最後の対戦の負け者
    loser = 0
    # 最後の対戦の勝者の番号
    winner_no = 0
    # 最後の対戦の負け者の番号
    loser_no = 0
    # 1回目の対戦の勝者
    winner1 = 0
    # 1回目の対戦の負け者
    loser1 = 0
    # 1回目の対戦の勝者の番号
    winner_no1 = 0
    # 1回目の対戦の負け者の番号
    loser_no1 = 0
    # 2回目の対戦の勝者
    winner2 = 0
    # 2回目の対戦の負け者
    loser2 = 0
    # 2回目の対戦の勝者の番号
    winner_no2 = 0
    # 2回目の対戦の負け者の番号
    loser_no2 = 0
    # 3回目の対戦の勝者
    winner3 = 0
    # 3回目の対戦の負け者
    loser3 = 0
    # 3回目の対戦の勝者の番号
    winner_no3 = 0
    # 3回目の対戦の負け者の番号
    loser_no3 = 0
    # 4回目の対戦の勝者
    winner4 = 0
    # 4回目の対戦の負け者
    loser4 = 0
    # 4回目
