Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    for i in range(N):
        B[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += (B[i] * (B[i] - 1)) // 2
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(N):
        mod[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*200
    for i in range(N):
        B[A[i]%200] += 1
    ans = 0
    for i in range(200):
        ans += B[i]*(B[i]-1)//2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = [0] * 200
    for i in range(N):
        cnt[A[i] % 200] += 1
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod_200 = [0] * 200
    for a in A:
        mod_200[a % 200] += 1

    ans = 0
    for m in mod_200:
        ans += m * (m - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i%200 for i in a]
    a.sort()
    ans = 0
    tmp = 0
    for i in range(1,n):
        if a[i] == a[i-1]:
            tmp += 1
        else:
            ans += tmp*(tmp+1)//2
            tmp = 0
    ans += tmp*(tmp+1)//2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(lambda x: int(x) % 200, input().split()))
    a.sort()
    #print(a)
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    #print(d)
    ans = 0
    for k in d:
        if d[k] > 1:
            ans += int(d[k] * (d[k] - 1) / 2)
    print(ans)
