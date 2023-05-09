def main():
    # 入力
    s = input()
    t = input()
    # 処理
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")
