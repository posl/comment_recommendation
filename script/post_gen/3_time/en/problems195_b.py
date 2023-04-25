Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = W // B
    max_oranges = W // A
    if W % B != 0:
        min_oranges += 1
    if W % A != 0:
        max_oranges -= 1
    if max_oranges < min_oranges:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)
main()

=======
Suggestion 2

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = W // B
    max_oranges = W // A
    if W % B != 0:
        min_oranges += 1
    if W % A != 0:
        max_oranges -= 1
    if min_oranges <= max_oranges:
        print(min_oranges, max_oranges)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 3

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
Suggestion 4

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = 0
    max_oranges = 0
    for i in range(1, W + 1):
        if A <= i <= B:
            if min_oranges == 0:
                min_oranges = i
            max_oranges = i
    if min_oranges == 0:
        print("UNSATISFIABLE")
    else:
        print(W // max_oranges, W // min_oranges)

=======
Suggestion 5

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = 0
    max_oranges = 0
    for i in range(1, W + 1):
        if W % i == 0 and A <= W / i <= B:
            min_oranges = i
            break
    for i in range(W, 0, -1):
        if W % i == 0 and A <= W / i <= B:
            max_oranges = i
            break
    if min_oranges == 0 and max_oranges == 0:
        print('UNSATISFIABLE')
    else:
        print(min_oranges, max_oranges)

=======
Suggestion 6

def main():
    a,b,w = map(int,input().split())
    w = w * 1000
    min = w // b
    max = w // a
    if w % b != 0:
        min += 1
    if w % a != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 7

def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min_orange = W//B
    max_orange = W//A
    if W%B != 0:
        min_orange += 1
    if min_orange <= max_orange:
        print(min_orange,max_orange)
    else:
        print("UNSATISFIABLE")

main()

=======
Suggestion 8

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_num, max_num = 0, 0
    for i in range(1, W+1):
        if A * i <= W <= B * i:
            min_num = i
            break
    for i in range(W, 0, -1):
        if A * i <= W <= B * i:
            max_num = i
            break
    if min_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)

=======
Suggestion 9

def main():
    A, B, W = map(int, input().split())
    W *= 1000

    min_oranges = -1
    max_oranges = -1

    for i in range(1, W+1):
        if A * i <= W <= B * i:
            min_oranges = i
            break

    for i in range(W, 0, -1):
        if A * i <= W <= B * i:
            max_oranges = i
            break

    if min_oranges == -1:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)

=======
Suggestion 10

def main():
    #input
    A, B, W = map(int, input().split())
    #compute
    W *= 1000
    min = W // B
    max = W // A
    if W % B > 0:
        min += 1
    if W % A > 0:
        max += 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)
