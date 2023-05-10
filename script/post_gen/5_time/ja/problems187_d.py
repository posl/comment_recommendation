Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_sum = sum(a)
    b_sum = sum(b)
    # print(a_sum, b_sum)
    if a_sum < b_sum:
        print(0)
        exit()
    diff = [a_i - b_i for a_i, b_i in zip(a, b)]
    # print(diff)
    diff.sort(reverse=True)
    # print(diff)
    count = 0
    for d in diff:
        count += 1
        a_sum -= d
        if a_sum < b_sum:
            break
    print(count)

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
    #print(a)
    #print(b)
    vote = []
    for i in range(n):
        vote.append(a[i]+b[i])
    #print(vote)
    vote.sort(reverse=True)
    #print(vote)
    aoki = 0
    takahashi = 0
    for i in range(n):
        if i%2 == 0:
            aoki += vote[i]
        else:
            takahashi += vote[i]
    #print(aoki)
    #print(takahashi)
    print(aoki - takahashi)

=======
Suggestion 3

def main():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    b_list.sort(reverse=True)
    b_sum = sum(b_list)
    a_sum = 0
    for i in range(n):
        a_sum += a_list[i]
        if a_sum > b_sum:
            print(i+1)
            exit()

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)

    # 青木氏の票の合計
    aoki = sum(A)
    #print(aoki)

    # 高橋氏の票の合計
    takahashi = 0
    for i in range(N):
        takahashi += B[i] * 2
    #print(takahashi)

    # 各町の高橋氏の票の差分
    diff = []
    for i in range(N):
        diff.append(A[i] + B[i] * 2)
    #print(diff)

    diff.sort(reverse=True)
    #print(diff)

    count = 0
    for i in range(N):
        if takahashi <= aoki:
            break
        takahashi -= diff[i]
        count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    for i in range(N):
        C.append(A[i] + B[i])
    C.sort()
    C.reverse()
    sum = 0
    count = 0
    for i in range(N):
        sum += C[i]
        count += 1
        if sum > sum / 2:
            break
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]

    ab.sort(key=lambda x: x[0] + x[0] + x[1], reverse=True)
    aoki = sum([x[0] for x in ab])
    takahashi = 0
    for i in range(N):
        aoki -= ab[i][0]
        takahashi += ab[i][0] + ab[i][1]
        if aoki < takahashi:
            print(i + 1)
            exit()

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
    ans = ans - min(a)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = sum(x[0] for x in AB)
    takahashi = 0
    ans = 0
    for i in range(N):
        aoki -= AB[i][0]
        takahashi += sum(AB[i])
        ans += 1
        if takahashi > aoki:
            break
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A,B = [],[]
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if N%2 == 1:
        print(B[N//2] - A[N//2] + 1)
    else:
        print(B[N//2]+B[N//2-1] - A[N//2]-A[N//2-1] + 1)

=======
Suggestion 10

def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0]+x[1], reverse=True)
    a_sum = sum([a for a, b in ab])
    b_sum = sum([b for a, b in ab])
    a_win = 0
    b_win = 0
    for a, b in ab:
        a_sum -= a
        b_sum -= b
        a_win += a
        b_win += b
        if a_win > b_sum:
            print(n - b_win)
            return
        if b_win > a_sum:
            print(n - a_win)
            return
    print(0)
    return
