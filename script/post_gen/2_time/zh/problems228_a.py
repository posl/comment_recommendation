Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    if N <= K:
        print(0)
    else:
        print(N-K)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i in range(n):
        if i < k:
            continue
        else:
            ans += a[i]

    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    # 一共有N个部门，K个部门组成一个项目
    # 所以一共有N//K个项目
    # 每个项目中的员工数为K个
    # 从A中选出K个员工，使得这K个员工的工号的最大值和最小值的差最小
    # 先选出一个员工，然后再选出K-1个员工
    # 选出的K-1个员工的工号必须在这个员工的工号的左右K-1个位置
    # 从左右K-1个位置中选出K-1个员工，使得这K-1个员工的工号的最大值和最小值的差最小
    # 从左右K-2个位置中选出K-2个员工，使得这K-2个员工的工号的最大值和最小值的差最小
    # 从左右K-3个位置中选出K-3个员工，使得这K-3个员工的工号的最大值和最小值的差最小
    # 从左右K-4个位置中选出K-4个员工，使得这K-4个员工的工号的最大值和最小值的差最小
    # ...
    # 从左右1个位置中选出1个员工，使得这1个员工的工号的最大值和最小值的差最小
    # 从左右0个位置中选出0个员工，使得这0个员工的工号的最大值和最小值的差最小
    # 这样就选出了K个员工，使得这K个员工的工号的最大值和最小值的差最小
    # 选出的K个员工的

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    print(sum(a[0:k]))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    print(n, k)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    #a.sort()
    #a.reverse()

    #print(a)

    #1. 1人しかいない部門がある場合、その部門は全てのプロジェクトに参加する
    #2. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数
    #3. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数
    #4. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数
    #5. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数
    #6. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数
    #7. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数
    #8. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプロジェクトの数

    #1. 1人しかいない部門がある場合、その部門は全てのプロジェクトに参加する
    if n == len(a):
        print(k)
        exit()

    #2. 1人しかいない部門がない場合、人数が最も少ない部門の人数が参加するプ

=======
Suggestion 8

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(A)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    for i in range(n-k):
        count += a[i]
    print(count)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    #print(A)
    #print(A[k-1])
    #print(A[:k])
    if A[k-1] == A[k]:
        print(n)
    else:
        print(k)
