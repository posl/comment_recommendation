def main():
    # 入力
    A, B, C = map(int, input().split())
    # 処理
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)
    return
