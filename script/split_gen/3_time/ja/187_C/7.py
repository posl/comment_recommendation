def main():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]
    # 処理
    S = set(S)
    for s in S:
        if '!' + s in S:
            print(s)
            exit()
    # 出力
    print('satisfiable')
