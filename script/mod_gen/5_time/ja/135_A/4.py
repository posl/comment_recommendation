def main():
    # -*- coding: utf-8 -*-
    # 整数の入力
    a, b = map(int, input().split())
    # スペース区切りの整数の入力
    #a, b = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{} {}".format(a+b+c, s))
    #print("{0} {1}".format(a+b+c, s))
    #print(f"{a+b+c} {s}")
    #print(f"{a+b+c=}, {s=}")
    #print(f"{a=}, {b=}")
    #print(f"{a=}")
    #print(f"{b=}")
    if (a - b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()