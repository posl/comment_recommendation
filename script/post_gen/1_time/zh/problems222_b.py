Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    print(sum([1 if P > a else 0 for a in A]))

=======
Suggestion 2

def main():
    #输入
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    #判断
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

main()

=======
Suggestion 4

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N,P = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in a:
        if i < P:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] < p:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    # N:学生人数
    # P:通过考试的分数
    N, P = map(int, input().split())
    # 学生成绩
    scores = list(map(int, input().split()))
    # 通过考试的学生人数
    pass_num = 0
    for score in scores:
        if score >= P:
            pass_num += 1
    # 不通过考试的学生人数
    fail_num = N - pass_num
    print(fail_num)

=======
Suggestion 8

def main():
    # N, P = input().split()
    # grades = input().split()
    # print(grades)
    # print(grades[0])
    # print(grades[1])
    # print(grades[2])
    # print(grades[3])
    # print(N)
    # print(P)
    # print(grades)
    # print(grades[0])
    # print(grades[1])
    # print(grades[2])
    # print(grades[3])
    # print(grades[4])
    # print(grades[5])
    # print(grades[6])
    # print(grades[7])
    # print(grades[8])
    # print(grades[9])
    # print(grades[10])
    # print(grades[11])
    # print(grades[12])
    # print(grades[13])
    # print(grades[14])
    # print(grades[15])
    # print(grades[16])
    # print(grades[17])
    # print(grades[18])
    # print(grades[19])
    # print(grades[20])
    # print(grades[21])
    # print(grades[22])
    # print(grades[23])
    # print(grades[24])
    # print(grades[25])
    # print(grades[26])
    # print(grades[27])
    # print(grades[28])
    # print(grades[29])
    # print(grades[30])
    # print(grades[31])
    # print(grades[32])
    # print(grades[33])
    # print(grades[34])
    # print(grades[35])
    # print(grades[36])
    # print(grades[37])
    # print(grades[38])
    # print(grades[39])
    # print(grades[40])
    # print(grades[41])
    # print(grades[42])
    # print(grades[43])
    # print(grades[44])
    # print(grades[45])
    # print(grades[46])
    # print(grades[47])
    # print(grades[48])
    # print(grades[49])
    # print(grades[50])
    # print(grades[51])
    # print(grades[52])
    #
