Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_orange = w // b
    max_orange = w // a
    if min_orange * a <= w <= max_orange * b:
        print(min_orange, max_orange)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 2

def main():
    a, b, w = map(int, input().split())
    w *= 1000

    min_oranges = w // b
    max_oranges = w // a
    if w % b != 0:
        min_oranges += 1
    if w % a != 0:
        max_oranges -= 1
    if min_oranges > max_oranges:
        print('UNSATISFIABLE')
    else:
        print(min_oranges, max_oranges)

=======
Suggestion 3

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_orange = 0
    max_orange = 0
    for i in range(1, W+1):
        if A*i <= W <= B*i:
            if min_orange == 0:
                min_orange = i
            max_orange = i
    if min_orange == 0:
        print('UNSATISFIABLE')
    else:
        print(min_orange, max_orange)

=======
Suggestion 4

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_orange = 10**9
    max_orange = 0
    for i in range(1, 1001):
        if A * i <= W <= B * i:
            min_orange = min(min_orange, i)
            max_orange = max(max_orange, i)
    if min_orange == 10**9:
        print('UNSATISFIABLE')
    else:
        print(min_orange, max_orange)

=======
Suggestion 5

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    if w % b == 0:
        mini = w // b
    else:
        mini = w // b + 1
    if w % a == 0:
        maxi = w // a
    else:
        maxi = w // a + 1
    if mini <= maxi:
        print(mini,maxi)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 6

def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min_oranges = W//B
    max_oranges = W//A
    if min_oranges*B < W:
        min_oranges += 1
    if max_oranges*A > W:
        max_oranges -= 1
    if min_oranges <= max_oranges:
        print(min_oranges,max_oranges)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 7

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    n = w//a
    m = w//b
    if n*b <= w <= m*a:
        print(n, m)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 8

def find_min_max_oranges(A,B,W):
    min_oranges = 0
    max_oranges = 0
    min_weight = A * 1000
    max_weight = B * 1000
    total_weight = W * 1000
    if min_weight > total_weight:
        return "UNSATISFIABLE"
    else:
        min_oranges = total_weight // max_weight
        max_oranges = total_weight // min_weight
        if total_weight % max_weight != 0:
            min_oranges += 1
        if total_weight % min_weight != 0:
            max_oranges += 1
        return str(min_oranges) + " " + str(max_oranges)

=======
Suggestion 9

def get_orange_count(A, B, W):
    W = W * 1000
    min_count = 0
    max_count = 0
    min_count = W // B
    if W % B != 0:
        min_count += 1
    max_count = W // A
    return min_count, max_count

=======
Suggestion 10

def main():
    # Read the input
    a, b, w = map(int, input().split())
    w *= 1000
    # If the range is too large, report that fact
    if a * 1000 > w:
        print("UNSATISFIABLE")
        return
    # Find the minimum and maximum possible numbers of oranges chosen
    min_oranges = 1000
    max_oranges = 0
    for i in range(1000):
        if a * i <= w and w <= b * i:
            min_oranges = min(min_oranges, i)
            max_oranges = max(max_oranges, i)
    # Output the result
    if min_oranges == 1000:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)
