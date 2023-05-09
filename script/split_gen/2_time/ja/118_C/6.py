def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 体力が最小のモンスターを選ぶ
    minA = min(A)
    # 体力が最小のモンスターの体力を出力
    print(minA)
