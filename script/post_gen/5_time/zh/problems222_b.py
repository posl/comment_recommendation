Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem222_b():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    fail = 0
    for i in range(n):
        if a[i] < p:
            fail += 1
    print(fail)

=======
Suggestion 2

def get_input():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    return n, p, a

=======
Suggestion 3

def main():
    line1 = input()
    line2 = input()
    line1 = line1.split()
    line2 = line2.split()

    N = int(line1[0])
    P = int(line1[1])
    a = []
    for i in range(N):
        a.append(int(line2[i]))

    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1

    print(count)

=======
Suggestion 4

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([1 for i in a if i < p]))

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
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N,P = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1
    print(count)

=======
Suggestion 8

def count_failed_students(students, pass_score):
    count = 0
    for student in students:
        if student < pass_score:
            count += 1
    return count
