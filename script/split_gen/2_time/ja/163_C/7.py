def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 直属の部下を数える
    subordinates = [0] * n
    for i in range(n - 1):
        subordinates[a[i] - 1] += 1
    # 結果を出力
    for i in range(n):
        print(subordinates[i])
