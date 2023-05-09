def main():
    N = int(input())
    x_y = []
    for i in range(N):
        a,b = map(int,input().split())
        x_y.append([a,b])
    x_y.sort()
    x = []
    y = []
    for i in range(N):
        x.append(x_y[i][0])
        y.append(x_y[i][1])
    x_count = []
    y_count = []
    x_count.append(1)
    y_count.append(1)
    for i in range(1,N):
        if x[i] == x[i-1]:
            x_count.append(x_count[i-1]+1)
        else:
            x_count.append(1)
        if y[i] == y[i-1]:
            y_count.append(y_count[i-1]+1)
        else:
            y_count.append(1)
    ans = 0
    for i in range(N):
        ans += x_count[i]*(x_count[i]-1)//2
        ans += y_count[i]*(y_count[i]-1)//2
    print(ans)
main()
問題文
N 個の整数 a_1,a_2,...,a_N が与えられます。a_1,a_2,...,a_N を 1 つ以上選んで、その和をとったときの和の最大値を求めてください。
制約
1 ≦ N ≦ 20
-10^9 ≦ a_i ≦ 10^9
入力はすべて整数である。
入力は全て 0 であることもありえる。
入力
入力は以下の形式で標準入力から与えられる。
N
a_1 a_2 ... a_N
出力
a_1,a_2,...,a_N を 1 つ以上選んで、その和をとったときの和の最大値を出力せよ。
入力例 1
4
-2 1 -4 3
出力例 1
4
入力例 2
5
-5 -3 -1 2 4
出力例 2
6
入力例 3
5
-1 -
