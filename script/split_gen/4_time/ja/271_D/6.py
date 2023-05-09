def main():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    # 1枚目のカードを表にするか裏にするかの組み合わせ
    for i in range(2):
        # 2枚目のカードを表にするか裏にするかの組み合わせ
        for j in range(2):
            # 3枚目のカードを表にするか裏にするかの組み合わせ
            for k in range(2):
                # 4枚目のカードを表にするか裏にするかの組み合わせ
                for l in range(2):
                    # 5枚目のカードを表にするか裏にするかの組み合わせ
                    for m in range(2):
                        sum = 0
                        if i == 0:
                            sum += cards[0][0]
                        else:
                            sum += cards[0][1]
                        if j == 0:
                            sum += cards[1][0]
                        else:
                            sum += cards[1][1]
                        if k == 0:
                            sum += cards[2][0]
                        else:
                            sum += cards[2][1]
                        if l == 0:
                            sum += cards[3][0]
                        else:
                            sum += cards[3][1]
                        if m == 0:
                            sum += cards[4][0]
                        else:
                            sum += cards[4][1]
                        if sum == S:
                            print('Yes')
                            if i == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if j == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if k == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if l == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if m == 0:
                                print('H')
                            else:
                                print('T')
                            exit()
    print('No')
