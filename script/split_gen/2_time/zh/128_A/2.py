def make_pie(apple, piece):
    if apple == 0:
        return 0
    elif piece == 1:
        return apple
    else:
        return apple // 2 + make_pie(apple - apple // 2 * 2, piece - 1)
