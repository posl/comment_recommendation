Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def cal():
    D,N = list(map(int,input().split()))
    if D==0:
        if N==100:
            return 101
        else:
            return N
    elif D==1:
        if N==100:
            return 10100
        else:
            return 100*N
    else:
        if N==100:
            return 1010000
        else:
            return 10000*N

print(cal())

=======
Suggestion 2

def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 3

def main():
    d, n = map(int, input().split())
    ans = (100 ** d) * n
    if n == 100:
        ans += 100 ** d
    print(ans)

=======
Suggestion 4

def main():
    d,n = map(int,input().split())
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(100*n)
    else:
        if n == 100:
            print(1010000)
        else:
            print(10000*n)

=======
Suggestion 5

def main():
    # 標準入力から2行取得
    line1 = input()
    line2 = input()
    # 1行目をスペースで分割し、int型に変換して変数に格納
    line1_split = line1.split(" ")
    D = int(line1_split[0])
    N = int(line1_split[1])
    # 2行目をスペースで分割し、int型に変換して変数に格納
    line2_split = line2.split(" ")
    a = int(line2_split[0])
    b = int(line2_split[1])
    # 100で割り切れる場合は100に変換
    if a == 100:
        a = 101
    # 100で割り切れる場合は100に変換
    if b == 100:
        b = 101
    # Dが0の場合はaをN回繰り返す
    if D == 0:
        print(a*N)
    # Dが1の場合はaをN回繰り返し、100倍する
    elif D == 1:
        print(a*N*100)
    # Dが2の場合はaをN回繰り返し、10000倍する
    else:
        print(a*N*10000)

=======
Suggestion 6

def main():
    d,n = map(int,input().split())
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    elif d == 2:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)

=======
Suggestion 7

def main():
    D, N = map(int, input().split())
    print(100**D * N)

=======
Suggestion 8

def main():
    d,n = map(int, input().split())
    if n == 100:
        n = 101
    print(100**d*n)
