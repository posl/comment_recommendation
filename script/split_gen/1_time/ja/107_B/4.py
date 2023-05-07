def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    a = list(map(list, zip(*a))) # 行列の転置
    a = [list(filter(lambda x: x != ".", x)) for x in a] # 行ごとに . を除去
    a = list(filter(lambda x: x != [], a)) # 空の行を除去
    a = list(map(list, zip(*a))) # 行列の転置
    a = [list(filter(lambda x: x != ".", x)) for x in a] # 行ごとに . を除去
    a = list(filter(lambda x: x != [], a)) # 空の行を除去
    for i in a:
        print("".join(i))
