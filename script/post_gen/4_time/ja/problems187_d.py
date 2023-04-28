Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    a_list.sort(reverse=True)
    b_list.sort(reverse=True)
    a_total = sum(a_list)
    b_total = sum(b_list)
    a_count = 0
    b_count = 0
    for a, b in zip(a_list, b_list):
        a_count += a
        b_count += b
        if b_count > a_total - a_count:
            print(n - a_list.index(a))
            break
    else:
        print(0)

=======
Suggestion 2

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = ans - max(A) + 1
    print(ans)
main()

=======
Suggestion 3

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if n % 2 == 1:
        print(b[n // 2] - a[n // 2] + 1)
    else:
        print((b[n // 2] + b[n // 2 - 1]) - (a[n // 2] + a[n // 2 - 1]) + 1)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n % 2 == 0:
        a_med = (a[n // 2 - 1] + a[n // 2]) // 2
        b_med = (b[n // 2 - 1] + b[n // 2]) // 2
    else:
        a_med = a[n // 2]
        b_med = b[n // 2]
    print(b_med - a_med + 1)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    A_sum = sum([AB[i][0] for i in range(N)])
    B_sum = sum([AB[i][1] for i in range(N)])
    A_cnt = 0
    B_cnt = 0
    for i in range(N):
        A_cnt += AB[i][0]
        B_cnt += AB[i][1]
        if A_cnt > B_sum - B_cnt:
            print(i+1)
            break

=======
Suggestion 7

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab = sorted(ab, key=lambda x: x[0]+x[1], reverse=True)
    a = sum([x[0] for x in ab])
    b = sum([x[1] for x in ab])
    ans = 0
    while a >= b:
        ans += 1
        a -= ab[ans-1][0]
        b -= ab[ans-1][1]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]+x[1], reverse=True)
    a_sum = sum([x[0] for x in ab])
    b_sum = 0
    ans = 0
    for x in ab:
        a_sum -= x[0]
        b_sum += x[0]+x[1]
        ans += 1
        if a_sum < b_sum:
            break
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    aoki = sum([ab[0] for ab in AB])
    takahashi = 0
    ans = 0
    for ab in AB:
        ans += 1
        aoki -= ab[0]
        takahashi += sum(ab)
        if takahashi > aoki:
            break
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    cnt = 0
    for a, b in AB:
        if a <= b:
            b -= a
            cnt += 1
            if b <= 0:
                break
        else:
            cnt += 1
            break
    print(cnt)
