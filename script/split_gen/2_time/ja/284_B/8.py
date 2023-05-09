def main():
    t = int(input()) #input()で標準入力から1行読み込み、int()で整数に変換
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        odd = 0
        for j in range(n):
            if a[j]%2 != 0:
                odd += 1
        print(odd)
