def main():
    # 入力を受け取る
    s, w = map(int, input().split())
    # 狼の数が羊の数以上なら unsafe
    if s <= w:
        print("unsafe")
    else:
        print("safe")
