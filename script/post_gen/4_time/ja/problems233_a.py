Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y - x) // 10)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
        return
    else:
        print((y - x) // 10)

=======
Suggestion 3

def main():
    x,y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(int((y-x)/10))

=======
Suggestion 4

def main():
    X,Y = map(int,input().split())
    if X >= Y:
        print(0)
    else:
        print((Y-X)//10)

=======
Suggestion 5

def solve():
    x, y = map(int, input().split())
    return max(0, (y - x) // 10)

print(solve())

=======
Suggestion 6

def solve():
    # x,y = map(int, input().split())
    x, y = 270, 750
    ans = 0
    if x == y:
        return ans
    if x > y:
        return ans
    if x < y:
        if x % 10 == 0:
            ans = (y - x) // 10
        else:
            ans = (y - x) // 10 + 1
    return ans

print(solve())
