Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                print("-1")
                return
        count += 1
        if len(set(A)) == 1:
            print(count)
            return

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            count += 1
            continue
        break
    if A.count(A[0]) == N:
        print(count)
    else:
        print(-1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                break
        else:
            ans += 1
            continue
        break
    while True:
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            ans += 1
            continue
        break
    if len(set(A)) == 1:
        print(ans)
    else:
        print(-1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt2 = 0
    cnt3 = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt2 += 1
        while a[i] % 3 == 0:
            a[i] /= 3
            cnt3 += 1
    if len(set(a)) == 1:
        print(max(cnt2,cnt3) - min(cnt2,cnt3))
    else:
        print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            else:
                break
        else:
            ans += 1
            continue
        break
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            ans += 1
            continue
        break
    if A.count(A[0]) == N:
        print(ans)
    else:
        print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 != 0:
                print(-1)
                return
            else:
                A[i] = A[i] // 2
        ans += 1
        if A.count(A[0]) == N:
            break
    print(ans - 1)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 2で割れる回数と3で割れる回数をそれぞれカウント
    count2 = 0
    count3 = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            count2 += 1
        while A[i] % 3 == 0:
            A[i] /= 3
            count3 += 1

    # 2で割れる回数と3で割れる回数が全て同じであれば、2で割れる回数を出力
    if count2 == count3:
        print(count2)
    else:
        print(-1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%2 if a%2 == 1 else a%3 if a%3 == 1 else a for a in A]
    if len(set(A)) == 1 and A[0] == 1:
        print(0)
    else:
        print(-1)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    count = 0
    while True:
        #print(A)
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                break
        else:
            count += 1
            continue
        break
    print(count)
