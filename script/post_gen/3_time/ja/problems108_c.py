Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    count = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                if a+b+b+c+c+a==3*K:
                    count += 1
    print(count)
main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if (a + b) % K == 0:
                ans += 1
    print(ans**3)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        if a % K == 0:
            ans += (N // K) ** 3
        elif a % K == K // 2:
            ans += (N // K) * ((N // K) + 1) ** 2
        else:
            ans += (N // K) * (N // K) * (N // K + 1)
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        if i%K == 0:
            ans += 1
    print(ans**3)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    # N,K = 3,2
    # N,K = 5,3
    # N,K = 31415,9265
    # N,K = 35897,932

    # 1以上N以下の正の整数の組 (a,b,c) であって、a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求める
    # ただし、a,b,c の順番を入れ替えただけの組も異なるものとして数える
    # また、a,b,c の中に同じものがあっても構わない

    # a,b,cの組み合わせは3*3*3=27通り
    # それぞれの合計がKの倍数であるかを判定する
    # 組み合わせは重複してカウントするので、Kの倍数の個数を求めて、27で割る

    # 1以上N以下の正の整数をKで割った余りを求める
    # 余りが0のものがKの倍数の個数
    # 余りが1のものがKの倍数の個数
    # 余りが2のものがKの倍数の個数
    # 余りが3のものがKの倍数の個数
    # 余りが4のものがKの倍数の個数
    # 余りが5のものがKの倍数の個数

    # 余りが0のものがKの倍数の個数
    # 余りが1のものがKの倍数の個数
    # 余りが2のものがKの倍数の個数
    # 余りが3のものがKの倍数の個数
    # 余りが4

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    ans = 0
    for a in range(1,N+1):
        b = a % K
        c = K - b
        if c == K:
            c = 0
        ans += (N//K)**3
        if b == 0:
            ans += (N//K + 1)**3
        if c == 0:
            ans += (N//K + 1)**3
        if b == c:
            ans -= (N//K + 1)**3
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        ans += (N//i)*(i//K)
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    ans = 0

    for i in range(1, N+1):
        ans += (N//i)*(i//K)
        if i%K == 0:
            ans += 1
        ans += max(0, N%i-K+1)
    print(ans)

=======
Suggestion 9

def main():
    n,k=map(int,input().split())
    mod=k
    count=0
    if k%2==0:
        for i in range(k//2+1,k):
            count+=((n//k)+1)*((n//k)+1)
        count+=((n//k)+1)*((n//k)+1)*(k//2)
    else:
        for i in range(1,k):
            count+=((n//k)+1)*((n//k)+1)
    print(count)
