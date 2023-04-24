Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    print((X // 500) * 1000 + ((X % 500) // 5) * 5)

=======
Suggestion 2

def main():
    X = int(input())
    print((X // 500) * 1000 + (X % 500) // 5 * 5)

=======
Suggestion 3

def main():
    X = int(input())
    ans = X // 500 * 1000
    ans += X % 500 // 5 * 5
    print(ans)

=======
Suggestion 4

def main():
    X = int(input())
    print(1000 * (X // 500) + 5 * ((X % 500) // 5))

=======
Suggestion 5

def main():
    x = int(input())
    if x == 0:
        print(0)
    else:
        print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 6

def main():
    x = int(input())
    print((x//500)*1000 + ((x%500)//5)*5)

=======
Suggestion 7

def main():
    X = int(input())
    print(X//500*1000 + X%500//5*5)

=======
Suggestion 8

def main():
    X = int(input())
    # 500円硬貨の枚数
    n = X // 500
    # 5円硬貨の枚数
    m = (X - n * 500) // 5
    print(n * 1000 + m * 5)

=======
Suggestion 9

def main():
    #入力
    X = int(input())
    #出力
    print((X//500)*1000 + ((X%500)//5)*5)
