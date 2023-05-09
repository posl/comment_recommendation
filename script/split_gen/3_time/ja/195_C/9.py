def main():
    N = int(input())
    # 1000 ごとにコンマが入るので、1000 で割った商がコンマの数になる
    print((len(str(N)) - 1) // 3)
