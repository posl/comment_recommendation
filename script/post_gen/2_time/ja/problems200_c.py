Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] - a[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]-A[j])%200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] % 200 == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if A[i] % 200 == 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    from collections import Counter
    C = Counter([a%200 for a in A])
    ans = 0
    for c in C.values():
        ans += c*(c-1)//2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    d = {}
    for i in range(N):
        m = A[i] % mod
        if m in d:
            d[m] += 1
        else:
            d[m] = 1
    ans = 0
    for k, v in d.items():
        if v >= 2:
            ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [i % 200 for i in A]
    cnt = 0
    for i in range(200):
        cnt += A.count(i) * (A.count(i) - 1) // 2
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    #print(A)
    c = [0]*200
    for a in A:
        c[a] += 1
    #print(c)
    ans = 0
    for i in range(200):
        ans += c[i]*(c[i]-1)//2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # A[i]を200で割った余りを取得
    A = [A[i] % 200 for i in range(N)]
    
    # 余りが同じものが何個あるかを数える
    from collections import Counter
    C = Counter(A)
    
    # 余りが同じものが2個以上ある場合、それらを2つ選ぶ組み合わせの数を求める
    ans = 0
    for v in C.values():
        if v >= 2:
            ans += v * (v - 1) // 2
    
    print(ans)
