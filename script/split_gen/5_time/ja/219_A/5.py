def problem219_a():
    #入力
    X = int(input())
    #処理
    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    elif X >= 90 and X <= 100:
        print('expert')
    else:
        print('入力された値が不正です。')
problem219_a()
