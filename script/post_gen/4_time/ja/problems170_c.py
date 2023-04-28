Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
        return
    if x not in p:
        print(x)
        return
    p.sort()
    for i in range(100):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return

=======
Suggestion 2

def main():
    x,n = map(int,input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int,input().split()))
    p.sort()
    if x not in p:
        print(x)
        return
    for i in range(1,101):
        if x-i not in p:
            print(x-i)
            return
        if x+i not in p:
            print(x+i)
            return

=======
Suggestion 3

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        elif x + i not in p:
            print(x + i)
            return

=======
Suggestion 4

def solve():
    x, n = map(int, input().split())
    if n == 0:
        return x
    p = list(map(int, input().split()))
    p.sort()
    if x not in p:
        return x
    for i in range(1, 100):
        if x - i not in p:
            return x - i
        elif x + i not in p:
            return x + i

=======
Suggestion 5

def main():
    x,n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    elif x not in p:
        print(x)
        return
    else:
        for i in range(1,101):
            if x-i not in p:
                print(x-i)
                return
            elif x+i not in p:
                print(x+i)
                return

=======
Suggestion 6

def solve():
    X, N = map(int, input().split())
    if N == 0:
        return X
    p = list(map(int, input().split()))
    if X not in p:
        return X
    else:
        for i in range(1, 100):
            if X - i not in p:
                return X - i
            elif X + i not in p:
                return X + i

=======
Suggestion 7

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(0, x + 1):
        if i not in p:
            print(i)
            return
        if x - i not in p:
            print(x - i)
            return

=======
Suggestion 8

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(0,100):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return

=======
Suggestion 9

def main():
    x,n = map(int,input().split())
    p = set(map(int,input().split()))
    if n == 0:
        print(x)
        return
    ans = 0
    for i in range(100):
        if not x - i in p:
            ans = x - i
            break
        if not x + i in p:
            ans = x + i
            break
    print(ans)

=======
Suggestion 10

def search_nearest_int(x, p_list):
    min_diff = 100
    for p in p_list:
        diff = abs(x - p)
        if diff < min_diff:
            min_diff = diff
            nearest_int = p
    return nearest_int
