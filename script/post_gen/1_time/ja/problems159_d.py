Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    sum = 0
    for i in range(1, n + 1):
        sum += cnt[i] * (cnt[i] - 1) // 2
    for i in range(n):
        print(sum - (cnt[a[i]] - 1))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    for i in range(N):
        if B[i] == 1:
            print(0)
        else:
            print(B[i] * (B[i] - 1) // 2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    #print(B)
    ans = [0] * N
    for i in range(N):
        if B[i] == 1:
            ans[i] = 0
        else:
            ans[i] = (B[i] * (B[i] - 1)) // 2
    #print(ans)
    for i in range(N):
        print((N - 1) * (N - 2) // 2 - ans[A[i] - 1] + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    d = {}
    for a in A:
        d[a] = d.get(a, 0) + 1
    for i in range(N):
        ans[i] = sum([d[a] for a in d if a != A[i]])
    for a in ans:
        print(a // 2)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    B = [0]*(N+1)
    for i in range(1,N+1):
        B[A[i]] += 1
    ans = [0]*(N+1)
    for i in range(1,N+1):
        ans[i] = (N-1) - (B[A[i]]-1)
    for i in range(1,N+1):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0 for i in range(N+1)]
    cnt = [0 for i in range(N+1)]
    for i in range(1, N+1):
        cnt[A[i]] += 1
    for i in range(1, N+1):
        ans[i] = cnt[A[i]] - 1
    #print(cnt)
    #print(ans)
    for i in range(1, N+1):
        print((N-1) - ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Aの要素数を数える
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1

    # Aの要素数を数える
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1

    # 答えを数える
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = cnt[i] * (cnt[i] - 1) // 2

    # 答えを出力する
    for i in range(1, N + 1):
        print(sum(ans) - ans[A[i - 1]] + (cnt[A[i - 1]] - 1) * (cnt[A[i - 1]] - 2) // 2)

=======
Suggestion 8

def main():
    n = int(input())
    A = list(map(int, input().split()))

    # Aの値をインデックスとするリストを作成
    B = [[] for _ in range(n)]
    for i in range(n):
        B[A[i]-1].append(i)

    # Bの要素数が1の場合は0を出力
    for i in range(n):
        if len(B[i]) == 1:
            print(0)
            exit()

    # Bの要素数が2の場合は1を出力
    for i in range(n):
        if len(B[i]) == 2:
            print(1)
            exit()

    # Bの要素数が3以上の場合は以下の処理を行う
    ans = []
    for i in range(n):
        if len(B[i]) >= 3:
            ans.append(len(B[i]) * (len(B[i])-1) // 2)

    # ansの要素数が1の場合は0を出力
    if len(ans) == 1:
        print(0)
        exit()

    # ansの要素数が2の場合は1を出力
    if len(ans) == 2:
        print(1)
        exit()

    # ansの要素数が3以上の場合は以下の処理を行う
    ans.sort()
    print(ans[0] + ans[1])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # aの各要素をインデックスとして、その要素の出現回数を��

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #Aの中に数字が何個あるかを記録する
    #Aの中に数字が何個あるかを記録する
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1

    #countの中から2個選ぶ組み合わせの数を求める
    count2 = [0] * (N+1) #countの中から2個選ぶ組み合わせの数
    for i in range(N+1):
        count2[i] = count[i] * (count[i] - 1) // 2

    #countの中から2個選ぶ組み合わせの数の合計
    count2sum = 0
    for i in range(N+1):
        count2sum += count2[i]

    #答えを求める
    for i in range(N):
        print(count2sum - count2[A[i]] + (count[A[i]] - 1) * (count[A[i]] - 2) // 2)
