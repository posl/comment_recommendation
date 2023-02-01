#問題文
#非負整数列 A=(a1,a2,…,aN) が与えられます。
#A の(添え字が相異なる) K 個の項の和として考えられる非負整数の集合を S とします。
#S に含まれる D の倍数の最大値を求めてください。ただし、S に D の倍数が含まれない場合、代わりに -1 と出力してください。
#
#制約
#1≤K≤N≤100
#1≤D≤100
#0≤ai≤10^9
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K D
#a1 … aN
#
#出力
#答えを出力せよ。
#
#入力例 1
#4 2 2
#1 2 3 4
#
#出力例 1
#6
#
#入力例 2
#3 1 2
#1 3 5
#
#出力例 2
#-1

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            s.add(sum(a[i:j]))
    ans = -1
    for i in s:
        if i % d == 0:
            ans = max(ans, i)
    print(ans)

if __name__ == '__main__':
    main()