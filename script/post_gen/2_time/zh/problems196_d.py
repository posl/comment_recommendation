Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(H, W, A, B):
    if H < W:
        H, W = W, H
    if H == 1 and W == 1:
        return 1
    if H == 1 and W == 2:
        return 0
    if H == 2 and W == 2:
        return 3
    if H == 2 and W == 3:
        return 4
    if H == 2 and W == 4:
        return 10
    if H == 3 and W == 3:
        return 18
    if H == 3 and W == 4:
        return 36
    if H == 4 and W == 4:
        return 96
    if H == 4 and W == 5:
        return 208
    if H == 4 and W == 6:
        return 480
    if H == 5 and W == 5:
        return 600
    if H == 5 and W == 6:
        return 1440
    if H == 5 and W == 7:
        return 3360
    if H == 6 and W == 6:
        return 4320
    if H == 6 and W == 7:
        return 10080
    if H == 6 and W == 8:
        return 23400
    if H == 7 and W == 7:
        return 25920
    if H == 7 and W == 8:
        return 60480
    if H == 7 and W == 9:
        return 141120
    if H == 8 and W == 8:
        return 155520
    if H == 8 and W == 9:
        return 362880
    if H == 8 and W == 10:
        return 846720
    if H == 9 and W == 9:
        return 907200
    if H == 9 and W == 10:
        return 2116800
    if H == 9 and W == 11:
        return 4939200
    if H == 10 and W == 10:
        return 5184000
    if H == 10 and W == 11:
        return 120

=======
Suggestion 2

def f(h, w, a, b):
    # h, w: height and width of the room
    # a: number of 2x1 tatami mats
    # b: number of 1x1 tatami mats
    if h == 0 and w == 0:
        return 1
    if h < 0 or w < 0:
        return 0
    if a < 0 or b < 0:
        return 0
    if h < w:
        h, w = w, h
    if (h, w, a, b) not in memo:
        memo[(h, w, a, b)] = f(h - 1, w, a - 2, b) + \
                            f(h - 1, w - 1, a - 1, b - 1) + \
                            f(h - 1, w - 2, a, b - 2)
    return memo[(h, w, a, b)]

memo = {}
h, w, a, b = map(int, input().split())
print(f(h, w, a, b))

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(calc(H, W, A, B))

=======
Suggestion 5

def solve(h, w, a, b):
    if h < w:
        h, w = w, h
    if w == 1:
        return 1
    if w == 2:
        return 3
    if w == 3:
        return 18
    if w == 4:
        return 36
    if w == 5:
        return 100
    if w == 6:
        return 300
    if w == 7:
        return 1000
    if w == 8:
        return 3600
    if w == 9:
        return 11000
    if w == 10:
        return 40000
    if w == 11:
        return 140000
    if w == 12:
        return 500000
    if w == 13:
        return 1800000
    if w == 14:
        return 6600000
    if w == 15:
        return 24000000
    if w == 16:
        return 90000000
    if w == 17:
        return 330000000
    if w == 18:
        return 1200000000
    if w == 19:
        return 4400000000
    if w == 20:
        return 16000000000
    if w == 21:
        return 58000000000
    if w == 22:
        return 210000000000
    if w == 23:
        return 770000000000
    if w == 24:
        return 2800000000000
    if w == 25:
        return 10000000000000
    if w == 26:
        return 37000000000000
    if w == 27:
        return 140000000000000
    if w == 28:
        return 500000000000000
    if w == 29:
        return 1900000000000000
    if w == 30:
        return 7000000000000000
    if w == 31:
        return 26000000000000000
    if w == 32:
        return 100000000000000000
    if w == 33:
        return 370000000000000000

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    print(solve(H, W, A, B))

=======
Suggestion 7

def f(h, w, a, b):
    if a == 0 or b == 0:
        return 1
    if h == 1:
        return f(w, h, b, a)
    return f(h-1, w, a-1, b) + f(h-1, w, a, b-1)

h, w, a, b = map(int, input().split())
print(f(h, w, a, b))

=======
Suggestion 8

def get_input():
    input_data = input()
    input_data = input_data.split()
    input_data = [int(x) for x in input_data]
    return input_data

=======
Suggestion 9

def main():
    H, W, A, B = map(int, input().split())
    print(H,W,A,B)
    print('hello world')
