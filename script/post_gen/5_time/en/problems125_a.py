Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t + 1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 2

def main():
    a, b, t = map(int, input().split())
    print(b * (t // a))

=======
Suggestion 3

def main():
    input_line = input()
    input_line = input_line.split()
    a = int(input_line[0])
    b = int(input_line[1])
    t = int(input_line[2])
    result = 0
    for i in range(1, t + 1):
        if i % a == 0:
            result += b
    print(result)

=======
Suggestion 4

def main():
    a, b, t = map(int, input().split())
    print((t // a) * b)

=======
Suggestion 5

def main():
    A, B, T = map(int, input().split())
    print(B * (T // A))

=======
Suggestion 6

def main():
    A, B, T = map(int, input().split())
    print((T//A)*B)

=======
Suggestion 7

def main():
    a, b, t = map(int, input().split())
    print(int(t // a * b))

=======
Suggestion 8

def count_biscuits(a, b, t):
    total_biscuits = 0
    for i in range(1, 1000000000):
        if a * i > t + 0.5:
            break
        total_biscuits += b
    return total_biscuits

=======
Suggestion 9

def main():
    a,b,t = map(int, input().split())
    print(int(t/a)*b)
