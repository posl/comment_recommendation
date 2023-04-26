Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))
    print(sum([abs(x) for x in X]))
    print(sum([abs(x)**2 for x in X])**(1/2))
    print(max([abs(x) for x in X]))

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(n)]))
    print(sum([x[i] ** 2 for i in range(n)]) ** 0.5)
    print(max([abs(x[i]) for i in range(n)]))

=======
Suggestion 3

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = list(map(abs, x))
    print(sum(x))
    print(sum([i**2 for i in x])**0.5)
    print(max(x))

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum(map(lambda x: x**2, x_abs))**0.5)
    print(max(x_abs))

=======
Suggestion 5

def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    x_list = [abs(x) for x in x_list]
    print(sum(x_list))
    print(sum([x**2 for x in x_list])**0.5)
    print(max(x_list))

=======
Suggestion 6

def main():
    N = int(input())
    x_list = list(map(int, input().split()))
    x_list_abs = [abs(x) for x in x_list]
    print(sum(x_list_abs))
    print(sum([x**2 for x in x_list_abs])**(1/2))
    print(max(x_list_abs))

=======
Suggestion 7

def problem180_b():
    N = int(input())
    x = list(map(int, input().split()))

    # マンハッタン距離
    m = 0
    for i in range(N):
        m += abs(x[i])

    # ユークリッド距離
    u = 0
    for i in range(N):
        u += x[i]**2
    u = u**0.5

    # チェビシェフ距離
    c = abs(x[0])
    for i in range(N):
        if c < abs(x[i]):
            c = abs(x[i])

    print(m)
    print(u)
    print(c)

=======
Suggestion 8

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 9

def manhattan_distance(x):
    return sum(map(abs, x))
