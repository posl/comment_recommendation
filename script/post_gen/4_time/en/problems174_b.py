Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if x ** 2 + y ** 2 <= D ** 2:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

main()

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X**2 + Y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x**2 + y**2)**(1/2) <= D:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x**2 + y**2) <= D**2:
            count += 1
    print(count)
