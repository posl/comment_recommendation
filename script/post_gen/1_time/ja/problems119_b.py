Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            ans += x
        else:
            ans += x * 380000
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    Y = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            Y += x
        else:
            Y += x * 380000.0
    print(Y)

main()

=======
Suggestion 3

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 4

def main():
    n = int(input())
    y = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            y += x
        else:
            y += x * 380000.0
    print(y)

=======
Suggestion 5

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            sum += x
        else:
            sum += x * 380000
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        x,u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x)*380000.0
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    yen = 0
    btc = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            yen += int(x)
        else:
            btc += float(x)
    print(yen + btc * 380000)

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(x_i)
        u.append(u_i)
    # 処理
    ans = 0
    for i in range(N):
        if u[i] == 'JPY':
            ans += int(x[i])
        else:
            ans += float(x[i])*380000.0
    # 出力
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_, u_ = input().split()
        x.append(x_)
        u.append(u_)
    ans = 0
    for i in range(N):
        if u[i] == "JPY":
            ans += int(x[i])
        else:
            ans += float(x[i]) * 380000.0
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    
    #合計金額の初期化
    total = 0
    
    #N人分の入力を受け取る
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        if u == "BTC":
            total += x * 380000.0
    
    #出力
    print(total)
