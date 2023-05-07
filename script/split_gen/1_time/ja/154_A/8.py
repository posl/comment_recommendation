def main():
    # 標準入力から1行取得
    s, t = input().split()
    a, b = input().split()
    u = input()
    if u == s:
        print(int(a)-1, b)
    elif u == t:
        print(a, int(b)-1)
    else:
        print(a, b)
