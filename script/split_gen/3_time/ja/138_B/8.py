def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1 / sum([1 / a for a in A]))
main()  # 出力結果：AC
