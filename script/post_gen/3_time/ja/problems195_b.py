Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if min <= max:
        print(min, max)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 2

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = w // b
    max = w // a
    if w % b != 0:
        min += 1
    if w % a != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 3

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    max = W // A
    min = W // B
    if W % B != 0:
        min += 1
    if max < min:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 4

def main():
    A, B, W = map(int, input().split())
    min = 1000
    max = 0
    for i in range(1, 1001):
        if A * i <= W * 1000 <= B * i:
            if min > i:
                min = i
            if max < i:
                max = i
    if min == 1000:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 5

def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 6

def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = W // B
    max = W // A
    if min * B <= W <= max * A:
        print(min, max)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 7

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_n = 0
    max_n = 0
    for i in range(1, W+1):
        if A * i <= W <= B * i:
            min_n = i
            break
    for i in range(W, 0, -1):
        if A * i <= W <= B * i:
            max_n = i
            break
    if min_n == 0 and max_n == 0:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)

=======
Suggestion 8

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 1001
    max = 0
    for i in range(A, B+1):
        if W % i == 0:
            if min > W // i:
                min = W // i
            if max < W // i:
                max = W // i
    if min == 1001:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 9

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_ans = W // B
    max_ans = W // A
    if min_ans * B <= W <= max_ans * A:
        print(min_ans, max_ans)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 10

def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    ans_min = W // B
    ans_max = W // A
    if ans_min * B > W:
        ans_min = ans_min + 1
    if ans_max * A < W:
        ans_max = ans_max - 1
    if ans_min > ans_max:
        print("UNSATISFIABLE")
    else:
        print(ans_min,ans_max)
