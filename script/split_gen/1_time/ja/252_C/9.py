def main():
    N = int(input())
    reels = [input() for _ in range(N)]
    # 10個のリールに対して、最初の文字が何秒で表示されるかを計算する
    # 0秒目に表示される文字は、0秒目に押されるボタンの次の文字
    # 1秒目に表示される文字は、1秒目に押されるボタンの次の文字
    # ...
    # 9秒目に表示される文字は、9秒目に押されるボタンの次の文字
    # 10秒目に表示される文字は、0秒目に押されるボタンの次の文字
    # 11秒目に表示される文字は、1秒目に押されるボタンの次の文字
    # ...
    # 19秒目に表示される文字は、9秒目に押されるボタンの次の文字
    # でも、10秒目に表示される文字は、0秒目に押されるボタンの次の文字
    # ということで、10秒目に表示される文字は、(0 + 10) % 10 文字目
    # 11秒目に表示される文字は、(1 + 10) % 10 文字目
    # ...
    # 19秒目に表示される文字は、(9 + 10) % 10 文字目
    # ということで、10秒目に表示される文字は、(0 + 10) % 10 文字目
    # 11秒目に表示される文字は、(1 + 10) % 10 文字目
    # ...
    # 19秒目に表示される文字は、(9 + 10) % 10 文字目
    # ということで、10秒目に表示される文字は、(0 + 10) % 10 文字目
    # 11秒目に表示される文字は、(1 + 10) % 10 文字目
