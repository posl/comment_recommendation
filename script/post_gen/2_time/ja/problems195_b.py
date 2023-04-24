Synthesizing 10/10 solutions (Duplicates hidden)

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
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 2

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_num = W // B
    max_num = W // A
    if W % B != 0:
        min_num += 1
    if W % A != 0:
        max_num -= 1
    if min_num > max_num:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)

=======
Suggestion 3

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 0
    max = 0
    for i in range(1, W + 1):
        if A * i <= W and W <= B * i:
            min = i
            break
    for i in range(1, W + 1):
        if A * i <= W and W <= B * i:
            max = i
    if min == 0 and max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 4

def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 5

def main():
    A,B,W = map(int,input().split())
    W = W * 1000
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
    min_num = 0
    max_num = 0
    for i in range(1, 1001):
        if A * i <= W * 1000 <= B * i:
            min_num = i
            break
    for j in range(1000, 0, -1):
        if A * j <= W * 1000 <= B * j:
            max_num = j
            break
    if min_num == 0 and max_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)

=======
Suggestion 7

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if A * max <= W <= B * max:
        print(min, max)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 8

def main():
    A,B,W = map(int,input().split())
    W = W*1000
    max = W//A
    min = W//B
    if W%A != 0:
        min += 1
    if W%B != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 9

def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = 1000000000
    max = 0
    for i in range(1, 1000000000):
        if A * i <= W <= B * i:
            if min > i:
                min = i
            if max < i:
                max = i
    if min == 1000000000:
        print("UNSATISFIABLE")
    else:
        print(min, max)
