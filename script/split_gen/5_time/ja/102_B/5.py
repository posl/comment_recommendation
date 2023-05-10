def main():
    # 整数の入力
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))
