Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    input_list = input().split()
    R = int(input_list[0])
    X = int(input_list[1])
    Y = int(input_list[2])
    return R, X, Y

=======
Suggestion 2

def problems198_c():
    return 0

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    r,x,y = map(int,input().split())
    if x**2+y**2 < r**2:
        print(2)
    else:
        print(int((x**2+y**2)**0.5/r)+1)

=======
Suggestion 5

def main():
    R, X, Y = map(int, input().split())
    if R * R > X * X + Y * Y:
        print(2)
    else:
        print(int((X * X + Y * Y) ** 0.5 // R) + 1)

=======
Suggestion 6

def problems198_c():
    pass

=======
Suggestion 7

def problem198_c():
    pass

=======
Suggestion 8

def solve():
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 < R**2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5 / R) + 1)
