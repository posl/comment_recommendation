Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]

    count = [0]*200
    for a in A:
        count[a] += 1

    ans = 0
    for c in count:
        ans += c*(c-1)//2
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= 200

    cnt = [0] * 200
    for i in range(N):
        cnt[A[i]] += 1

    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2

    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)

    # 200で割った余りの数を格納するための配列
    # 余りが0の時は、0番目に入れる
    # 余りが1の時は、1番目に入れる
    # 余りが2の時は、2番目に入れる
    # ...
    # 余りが199の時は、199番目に入れる
    # 余りが200の時は、0番目に入れる
    # 余りが201の時は、1番目に入れる
    # ...
    # 余りが399の時は、199番目に入れる
    # 余りが400の時は、0番目に入れる
    # 余りが401の時は、1番目に入れる
    # ...
    # 余りが599の時は、199番目に入れる
    # 余りが600の時は、0番目に入れる
    # ...
    # 余りが999の時は、199番目に入れる
    # 余りが1000の時は、0番目に入れる
    # ...
    # 余りが1999の時は、199番目に入れる
    # 余りが2000の時は、0番目に入れる
    # ...
    # 余りが999999999の時は、199番目に入れる
    # 余りが1000000000の時は、0番目に入れる
    # ...
    # 余りが1000000199の時は、199番目に入れる
    # 余りが1000000200の時は、0番目に入れる
    # ...
    # 余りが1000000399の時は、199番目に入れる
    # 余りが1000000400の時は、0番目に入れる
    # ...
    # 余

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0]*200
    for i in range(n):
        cnt[a[i]%200] += 1
    for i in range(200):
        ans += (cnt[i]*(cnt[i]-1))//2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = [0] * 200
    for i in range(n):
        r[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += r[i] * (r[i] - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        a[i] %= 200
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for key in d:
        ans += d[key] * (d[key] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_mod = [i % 200 for i in a]
    a_mod.sort()
    ans = 0
    cnt = 1
    for i in range(n - 1):
        if a_mod[i] == a_mod[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(n):
        mod[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in a:
        b[i % 200] += 1
    ans = 0
    for i in b:
        ans += i * (i - 1) // 2
    print(ans)
