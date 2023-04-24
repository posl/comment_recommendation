Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        if A[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if A[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] == 1:
            ans += 1
            continue
        if A[i] - A[i - 1] == 1:
            ans += 1
            continue
        if A[i] - A[i - 1] > 1:
            print(-1)
            return
    print(N - ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] > A[i-1] + 1:
            print(-1)
            return
        elif A[i] == A[i-1] + 1:
            ans += 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == ans + 1:
            ans += 1
    if ans == 0:
        print(-1)
    else:
        print(N - ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
    else:
        ans = 0
        for i in range(N-1):
            if A[i+1] - A[i] > 1:
                print(-1)
                return
            elif A[i+1] == A[i] + 1:
                ans += 1
            else:
                ans += A[i+1]
        print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 1:
        print(-1)
        return
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            continue
        elif A[i] + 1 == A[i + 1]:
            continue
        else:
            print(-1)
            return
    print(N - A[-1])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(N):
        if B[i + 1] == 0:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))

    # 最小値を求める
    min_a = min(a)

    # 最小値のindexを求める
    min_a_index = a.index(min_a)

    # 最小値のindexより左側の値を切り取る
    a = a[min_a_index:]

    # 最小値のindexより右側の値を切り取る
    a = a[:N]

    # 最小値からNまでの値を求める
    min_a_to_N = list(range(min_a, N + 1))

    # 最小値からNまでの値とaの値が一致しているかを確認する
    if min_a_to_N == a:
        print(min_a_index)
    else:
        print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #A[i]がi+1でなければ、A[i]をi+1にするために、A[i]の位置までの距離を求める
    #その距離を総和すると、A[i]をi+1にするために必要な最小のブロックの数が求められる
    #これをすべてのA[i]について実行すると、最小のブロックの数が求まる
    #ただし、A[i]がi+1でない場合は、A[i]の位置までの距離が求められないので、
    #その場合は、-1を出力する

    #A[i]がi+1でない場合の最小のブロックの数
    min_block = 0

    #A[i]がi+1でない場合の最小のブロックの数を求める
    for i in range(N):
        if A[i] != i+1:
            min_block += 1

    #A[i]がi+1でない場合の最小のブロックの数がN-1より大きい場合、
    #A[i]がi+1でない場合の最小のブロックの数は求められない
    if min_block > N-1:
        print(-1)
        return

    #A[i]がi+1でない場合の最小のブロックの数を求める
    for i in range(N):
        #A[i]がi+1でない場合
        if A[i] != i+1:
            #A[i]の位置までの距離を求める
            distance = A[i] - i - 1

            #A[i]がi+1でない場合の最小のブロックの数がN-1より大きい場合、
            #A[i]が

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    #print(n)
    #print(a)
    #print(sorted(a))
    #print(sorted(a) == list(range(1, n+1)))
    if sorted(a) == list(range(1, n+1)):
        print(0)
        return
    if a[0] != 1:
        print(-1)
        return
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i
    #print(b)
    max = 0
    for i in range(n):
        if b[i] > max:
            max = b[i]
        if max < i:
            print(-1)
            return
    print(n - max - 1)

main()
