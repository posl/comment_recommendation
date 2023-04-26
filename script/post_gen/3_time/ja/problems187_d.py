Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N - 1, -1, -1):
        a = A[i]
        b = B[i]
        if (a + ans) % b != 0:
            ans += b - ((a + ans) % b)
    print(ans)

=======
Suggestion 2

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
    #print(a)
    #print(b)
    a_count = 0
    b_count = 0
    for i in range(n):
        #print(a_count, b_count)
        if a_count > b_count:
            b_count += b[i]
        else:
            a_count += a[i]
        #print(a_count, b_count)
    if a_count > b_count:
        print(n)
    else:
        print(n-1)

=======
Suggestion 3

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab = sorted(ab, key=lambda x:x[0]+x[1], reverse=True)
    a_sum = 0
    b_sum = 0
    for i in range(n):
        a_sum += ab[i][0]
    ans = 0
    for i in range(n):
        a_sum -= ab[i][0]
        b_sum += ab[i][0]+ab[i][1]
        ans += 1
        if a_sum < b_sum:
            break
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum < b_sum:
        print(0)
        return
    i = 0
    j = 0
    ans = 0
    while i < n and j < n:
        if a[i] > b[j]:
            ans += 1
            i += 1
        else:
            j += 1
    print(ans+1)

=======
Suggestion 5

def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))

    AB.sort(key=lambda x: x[0] + x[1], reverse=True)

    A_sum = 0
    B_sum = 0
    for i in range(N):
        A_sum += AB[i][0]
        B_sum += AB[i][1]
        if A_sum < B_sum:
            print(i + 1)
            return
    print(N)

=======
Suggestion 6

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = sum([i[0] for i in AB])
    takahashi = 0
    ans = 0
    for i in range(N):
        aoki -= AB[i][0]
        takahashi += AB[i][0] + AB[i][1]
        ans += 1
        if aoki < takahashi:
            break
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    a_sum = sum([a for a, _ in ab])
    b_sum = sum([b for _, b in ab])
    ab_diff = [(a - b) for a, b in ab]
    ab_diff.sort(reverse=True)

    if a_sum < b_sum:
        print(0)
        exit()

    diff_sum = 0
    for i in range(n):
        diff_sum += ab_diff[i]
        if diff_sum >= 0:
            print(i + 1)
            exit()

=======
Suggestion 8

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = sum([ab[i][0] for i in range(n)])
    takahashi = 0
    for i in range(n):
        aoki -= ab[i][0]
        takahashi += ab[i][0] + ab[i][1]
        if takahashi > aoki:
            print(i+1)
            break

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    A = 0
    B = 0
    for i in range(N):
        if i % 2 == 0:
            A += AB[i][0]
        else:
            B += AB[i][1]
    print(A-B)

=======
Suggestion 10

def solve():
    N = int(input())
    towns = []
    for i in range(N):
        A, B = map(int, input().split())
        towns.append((A, B, A + B))
    towns.sort(key=lambda x: x[2], reverse=True)
    A_sum = sum([t[0] for t in towns])
    B_sum = 0
    ans = 0
    for i in range(N):
        A_sum -= towns[i][0]
        B_sum += towns[i][2]
        ans += 1
        if B_sum > A_sum:
            break
    print(ans)
