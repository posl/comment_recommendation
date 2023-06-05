Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n,p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 3

def count_student(N,P,student_score):
    count = 0
    for i in range(N):
        if student_score[i] < P:
            count += 1
    return count

=======
Suggestion 4

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N,P = input().split()
    N = int(N)
    P = int(P)
    a = input().split()
    count = 0
    for i in range(N):
        if int(a[i]) < P:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N,P = map(int,input().split())
    a = list(map(int,input().split()))
    print(len(list(filter(lambda x:x<P,a))))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def solve():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] < p:
            ans += 1
    print(ans)

=======
Suggestion 9

def get_input():
    input_list = []
    while True:
        try:
            line = input()
            if line == "":
                break
            else:
                input_list.append(line)
        except EOFError:
            break
    return input_list

=======
Suggestion 10

def main():
    #input
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    #count
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    #output
    print(count)
