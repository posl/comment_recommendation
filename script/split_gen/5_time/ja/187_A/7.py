def main():
    # 標準入力受付
    a, b = map(int, input().split())
    # print(a, b)
    # 処理
    sa = sum(list(map(int, list(str(a)))))
    sb = sum(list(map(int, list(str(b)))))
    if sa > sb:
        print(sa)
    else:
        print(sb)
