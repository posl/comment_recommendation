def main():
    X = input()
    M = int(input())
    #Xを10進数で見たときの最大の数
    max = 0
    for i in X:
        if max < int(i):
            max = int(i)
    #max+1以上の数で、Xをn進数で見たときの数がM以下のnの個数をカウント
    count = 0
    for i in range(max+1, M+1):
        total = 0
        for j in range(len(X)):
            total += int(X[j]) * pow(i, len(X)-j-1)
        if total <= M:
            count += 1
    #M以下の数の個数
    print(count)
