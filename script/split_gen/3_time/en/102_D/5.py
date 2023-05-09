def main():
    N = int(input())
    A = list(map(int, input().split()))
    #累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #print(S)
    #最小値と最大値の差を求める
    def calc(x):
        return max(S[x + 1], S[N] - S[x + 1]) - min(S[x + 1], S[N] - S[x + 1])
    #print(calc(0))
    #print(calc(1))
    #print(calc(2))
    #最小値と最大値の差が最小になる場所を求める
    #最小値と最大値の差が最小になる場所は、最小値と最大値の差を求める際に使った累積和の値が最小になる場所である
    #S[x + 1]が最小になる場所を求める
    #S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x]が最大になる場所は、S[x]が最大になる場所は、S[x + 1]が最小になる場所である
    #S[x + 1]が最小になる場所は、S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x + 1]が最小になる場所は、S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x + 1]が最小になる場所は、S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x + 1
