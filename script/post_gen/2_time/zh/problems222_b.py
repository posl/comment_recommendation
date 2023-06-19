Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i < P:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1
    print(count)

=======
Suggestion 3

def get_input():
    #input_str = input()
    #input_str = "4 50\n80 60 40 0"
    #input_str = "3 90\n89 89 89"
    input_str = "2 22\n6 37"
    input_list = input_str.split("\n")
    #print(input_list)
    #print(input_list[0])
    #print(input_list[1])
    #print(input_list[2])
    #print(input_list[3])
    return input_list

=======
Suggestion 4

def get_input():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    return n,p,a

=======
Suggestion 5

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1

    print(count)

=======
Suggestion 6

def main():
    # 读入N和P
    N, P = map(int, input().split())
    # 读入a_1, a_2, ..., a_N
    a = list(map(int, input().split()))
    # 用来存储能够通过考试的学生的人数
    ans = 0
    # 用来存储未能通过考试的学生的人数
    dis = 0
    # 用来存储能够通过考试的学生的人数
    for i in range(N):
        if a[i] >= P:
            ans += 1
        else:
            dis += 1
    # 输出结果
    print(dis)

=======
Suggestion 7

def isPass(score, pass_score):
    if score >= pass_score:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)
