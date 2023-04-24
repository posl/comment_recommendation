Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i]+L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if li[i] != li[j] and li[j] != li[k] and li[k] != li[i] and li[i] + li[j] > li[k]:
                    count += 1
    print(count)

=======
Suggestion 5

def check(a,b,c):
    if a == b or b == c or c == a:
        return False
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(L[i],L[j],L[k]):
                ans += 1
print(ans)

=======
Suggestion 6

def check(a,b,c):
    if a != b and b != c and c != a:
        if a+b > c and b+c > a and c+a > b:
            return True
    return False

N = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(L[i],L[j],L[k]):
                ans += 1
print(ans)

=======
Suggestion 7

def main():
    # 標準入力から整数値を取得する
    n = int(input())
    # 標準入力から整数値を取得してリストに格納する
    l = list(map(int, input().split()))
    # 結果を格納する変数
    r = 0
    # 三角形を作ることのできるような長さの異なる 3 本の棒を選ぶ方法を全て調べる
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 三角形の成立条件を満たすかどうか調べる
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    # 三角形の成立条件を満たす場合は結果に 1 を加算する
                    r += 1
    # 結果を出力する
    print(r)
