def main():
    N = int(input())
    # 1 以上 2N+1 以下の整数のうち、すでに宣言された整数を記録するリスト
    declared = []
    # 先手は 1 以上 2N+1 以下の整数のうち、最小の整数を宣言する
    declared.append(1)
    print(1)
    # ゲームが終了するまでループ
    while True:
        # 青木君の宣言を受け取る
        aoki = int(input())
        # 青木君が宣言した整数を記録する
        declared.append(aoki)
        # 高橋君が宣言する整数を決定する
        takahashi = min(set(range(1, 2*N+2)) - set(declared))
        # 高橋君が宣言した整数を記録する
        declared.append(takahashi)
        # 高橋君が宣言した整数を出力する
        print(takahashi)
        # 青木君が宣言できる整数が残っていない場合はゲームを終了する
        if takahashi == 2*N+1:
            break
