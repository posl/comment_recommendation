def min_money(n, m, list):
    list.sort(key=lambda x: (x[0], -x[1]))
    i = 0
    money = 0
    while m > 0:
        if list[i][1] >= m:
            money += m * list[i][0]
            break
        else:
            money += list[i][1] * list[i][0]
            m -= list[i][1]
            i += 1
    print(money)

if __name__ == '__main__':
    min_money()