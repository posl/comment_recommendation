def main():
    s = input()
    # 1文字目から順番に、最後の文字から順番に比較していく。
    # 一致していれば、次の文字へ。
    # 不一致であれば、最後の文字を一致させるように変更する。
    # 1文字目が最後の文字へ変更されたときに、
    # 2文字目から最後から2文字目までが回文になっていれば、
    # 1文字目の変更回数は1回になる。
    # そうでなければ、2回になる。
    # 1文字目の変更回数が2回を超えることはない。
    # 1文字目が最後の文字へ変更されたときに、
    # 2文字目から最後から2文字目までが回文になっていなければ、
    # 1文字目の変更回数は2回になる。
    # そうでなければ、3回になる。
    # 1文字目が最後の文字へ変更されたときに、
    # 2文字目から最後から2文字目までが回文になっていなければ、
    # 1文字目の変更回数は3回になる。
    # そうでなければ、4回になる。
    # 1文字目が最後の文字へ変更されたときに、
    # 2文字目から最後から2文字目までが回文になっていなければ、
    # 1文字目の変更回数は4回になる。
    # そうでなければ、5回になる。
    # 1文字目が最後の文字へ変更されたときに、
    # 2文字目から最後から2文字目までが回文になっていな

if __name__ == '__main__':
    main()