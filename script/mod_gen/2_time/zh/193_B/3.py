def get_min_money(N, shops):
    min_money = -1
    for i in range(N):
        if shops[i][2] > 0:
            if min_money == -1:
                min_money = shops[i][1]
            else:
                if shops[i][1] < min_money:
                    min_money = shops[i][1]
    return min_money

if __name__ == '__main__':
    get_min_money()