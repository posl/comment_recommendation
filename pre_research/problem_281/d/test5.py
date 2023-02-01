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
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") == K:
            S.add(sum([A[j] for j in range(N) if (i >> j) & 1]))
    ans = -1
    for s in S:
        if s % D == 0:
            ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()