def get_all_patterns(h, w):
    # 縦線の数がw本の時のあみだくじのパターン数を返す
    # ただし、縦線の数が1本の時は、横線を引けないので、パターン数は1
    if w == 1:
        return 1
    else:
        # 縦線の数がw-1本の時のあみだくじのパターン数を返す
        # ただし、横線を引けない位置には縦線を引くことができないので、
        # 縦線の数がw-2本の時のあみだくじのパターン数を返す
        return get_all_patterns(h, w-1) + get_all_patterns(h, w-2)
