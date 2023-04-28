Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5):
        ans = max(ans, b[i] + b[i + 1] + b[i + 2])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*(10**5)+1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2*(10**5)+1):
        ans += b[i]%2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(n):
        ans[a[i]-1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(n):
        ans[a[i]-1] += 1
    for i in range(n):
        print(ans[i])
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ball = [0] * (2 * 10 ** 5 + 1)
    ans = []
    for i in range(n):
        ball[a[i]] += 1
        if ball[a[i]] == 2:
            ball[a[i]] = 0
        ans.append(sum(ball))
    print(*ans, sep="\n")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        s.add(a[i])
        while True:
            if a[i] in s:
                a[i] += 1
            else:
                break
        print(a[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(0)
    for i in range(N):
        ans[A[i] - 1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    cnt = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        ans[i] = i + 1 - cnt[a[i]]
        cnt[a[i]] += 1
    print(*ans, sep='\n')

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(1)
    ans.reverse()
    ans[0] = a[0]
    for i in range(1, n):
        if ans[i-1] == a[i]:
            ans[i] = 0
        else:
            ans[i] = a[i]
    ans.reverse()
    for i in range(n):
        if ans[i] == 0:
            ans[i] = ans[i-1]
    for i in range(n):
        print(ans[i])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 連続しているボールの個数をカウントする
    cnt = [0] * 200010

    # 1個目のボールを落とす
    cnt[a[0]] += 1

    # 2個目以降のボールを落とす
    for i in range(1, n):
        # 2個目以降のボールを落とす前に、筒の中にあるボールに書かれた整数は下から順に何個あるかを求める
        ans = 0
        for j in range(200010):
            if cnt[j] > 0:
                ans += 1

        # 2個目以降のボールを落とす
        cnt[a[i]] += 1

        # 2個目以降のボールを落とした後、筒の中にあるボールに書かれた整数は下から順に何個あるかを求める
        ans2 = 0
        for j in range(200010):
            if cnt[j] > 0:
                ans2 += 1

        print(ans2 - ans)
