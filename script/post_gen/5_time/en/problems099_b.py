Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    sum = 0
    for i in range(1, 1000):
        sum += i
        if sum - a == b - sum:
            print(sum - a)
            exit()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    x = b - a
    y = (x * (x + 1)) // 2
    print(y - b)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(int((b-a)*(b-a+1)/2 - b))

=======
Suggestion 5

def main():
    a, b = list(map(int, input().split()))
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    print(sum(range(1,b-a))-b)

=======
Suggestion 7

def snow_cover(a, b):
    return b - a
