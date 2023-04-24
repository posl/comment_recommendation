Synthesizing 10/10 solutions

=======
Suggestion 1

def round_down(num, divisor):
    return num - (num%divisor)

X, K = map(int, input().split())

for i in range(K):
    X = round_down(X, 10**(i+1))

print(X)

=======
Suggestion 2

def main():
    x, k = map(int, input().split())
    for i in range(k):
        x = round(x, -i)
    print(x)

=======
Suggestion 3

def round_down(num, divisor):
    return num - (num%divisor)

X,K = map(int,input().split())
for i in range(K):
    X = round_down(X,10**i)
print(X)

=======
Suggestion 4

def round_down(num, divisor):
    return num - (num%divisor)

x,k = map(int, input().split())
for i in range(k):
    x = round_down(x, 10**i)
print(x)

=======
Suggestion 5

def main():
    X,K=map(int,input().split())
    for i in range(K):
        X=round(X,-(i+1))
    print(X)

=======
Suggestion 6

def round_down(num, divisor):
    return num - (num%divisor)

=======
Suggestion 7

def main():
    X, K = map(int, input().split())
    d = 10**K
    print((X + d // 2) // d * d)

=======
Suggestion 8

def main():
    X,K = map(int,input().split())
    X = list(str(X))
    X.reverse()
    for i in range(K):
        if int(X[i]) >= 5:
            if i == K-1:
                X[i] = "0"
                X.append("1")
            else:
                X[i] = "0"
                X[i+1] = str(int(X[i+1])+1)
    X.reverse()
    print("".join(X))

=======
Suggestion 9

def main():
    X, K = map(int, input().split())
    #print(X, K)
    #print(X % 10**K)
    #print(X % 10**K >= 5 * 10**(K-1))
    if X % 10**K >= 5 * 10**(K-1):
        print(X + 10**K - X % 10**K)
    else:
        print(X - X % 10**K)
    return

=======
Suggestion 10

def main():
    X, K = map(int, input().split())
    ans = 0
    # 10^i の位以下を四捨五入する
    # 10^i の位を取得
    # 10^i を超える桁を取得
    # 10^i で割った余りを取得
    # 10^i で割った商を取得
    # 10^i の位以下の桁を取得
    # 10^i の位以下の桁を四捨
