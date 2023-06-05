Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = sorted(a)
    print(a.index(b[1])+1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # a = [1, 123, 12345, 12, 1234, 123456]
    # a = [3, 1, 4, 15, 9]
    b = sorted(a)
    print(a.index(b[1]) + 1)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m1 = min(a)
    m2 = min([x for x in a if x != m1])
    print(a.index(m2) + 1)

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    print(a.index(b[1])+1)

=======
Suggestion 6

def getSecondLowestScorePlayerIndex(scores):
    """获取第二低分玩家的索引"""
    # 先排序
    scores.sort(reverse=True)
    # 找到第二低分
    secondLowestScore = scores[0]
    for score in scores:
        if score < secondLowestScore:
            secondLowestScore = score
            break
    # 找到第二低分玩家的索引
    for index, score in enumerate(scores):
        if score == secondLowestScore:
            return index

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[1])+1)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[1]) + 1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    print(A[1])
