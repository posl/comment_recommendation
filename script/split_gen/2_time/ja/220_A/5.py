def main():
    #入力
    A, B, C = map(int, input().split())
    #Cの倍数をリストに格納
    multiples = [i for i in range(A, B + 1) if i % C == 0]
    #リストが空なら-1を出力
    if not multiples:
        print(-1)
    #リストが空でないなら最小値を出力
    else:
        print(min(multiples))
