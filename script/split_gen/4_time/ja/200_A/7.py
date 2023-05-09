def problem200_a(input):
    # 処理を書く
    N = int(input)
    century = N // 100
    if N % 100 == 0:
        return century
    else:
        return century + 1
