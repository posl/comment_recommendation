def main():
    # 整数の入力
    a, b, c = map(int, input().split())
    print(a+b+c+max(a,b,c)*9)
