def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print('No')
        return
    # Sのそれぞれの文字を、Tの何番目の文字からスタートするかを記録する
    # 例えば、S = 'abbaac'、T = 'abbbbaaac'の場合、
    # SのaはTの1文字目からスタートする
    # SのbはTの4文字目からスタートする
    # SのcはTの9文字目からスタートする
    # という具合になる
    # そのため、Sの文字を1文字ずつ見ていき、Tの何番目の文字からスタートするかを記録していく
    # このとき、Tの文字を1文字ずつ見ていく
    # 例えば、SのaはTの1文字目からスタートする
    # この時、Tの1文字目はaなので、Tの2文字目からスタートする
    # このように、Sの文字を1文字ずつ見ていくと、Tの文字を1文字ずつ見ていくことになる
    # このように、Sの文字を1文字ずつ見ていくと、Tの文字を1文字ずつ見ていくことになる
    # そのため、Sの文字を1文字ずつ見ていくと、Tの文字を1文字ずつ見ていくことになる
    # このように、Sの文字を1文字ずつ見ていくと、Tの文字を1文字ずつ見ていくことになる
    # そのため、Sの文字を1文字ずつ見ていくと、Tの文字を1文字ずつ見ていくことになる
    # このように、Sの文字を1文字ずつ見ていくと、Tの文字を1文字
