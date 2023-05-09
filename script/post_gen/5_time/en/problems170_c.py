Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    if n == 0:
        print(x)
        return
    if x not in p:
        print(x)
        return
    for i in range(1, 100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 2

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    if x not in p:
        print(x)
        return
    for i in range(1,100):
        if x - i not in p:
            print(x-i)
            return
        elif x + i not in p:
            print(x+i)
            return

=======
Suggestion 3

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(1, 100):
        if x - i not in p:
            print(x - i)
            return
        elif x + i not in p:
            print(x + i)
            return

=======
Suggestion 4

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(1, 101):
        if not i in p:
            if abs(x - i) < abs(x - p[0]):
                print(i)
                return
            elif abs(x - i) == abs(x - p[0]):
                print(min(i, p[0]))
                return
            else:
                print(p[0])
                return
    print(p[0])
    return

=======
Suggestion 5

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        exit()
    p = sorted(map(int, input().split()))
    for i in range(100):
        if x - i not in p:
            print(x - i)
            exit()
        if x + i not in p:
            print(x + i)
            exit()

=======
Suggestion 6

def main():
    x, n = map(int, input().split())
    p = [int(i) for i in input().split()]
    if n == 0:
        print(x)
        return
    p.sort()
    if x not in p:
        print(x)
        return
    for i in range(1, 100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 7

def main():
    x,n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(1,100):
        if not i in p:
            if abs(x-i) < abs(x-p[0]):
                print(i)
                return
            elif abs(x-i) == abs(x-p[0]):
                print(min(i,p[0]))
                return
    print(p[0])
    return

=======
Suggestion 8

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    diff = 100
    ans = 100
    for i in range(102):
        if i not in p and diff > abs(x - i):
            diff = abs(x - i)
            ans = i
    print(ans)

=======
Suggestion 9

def solution():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(1, 100):
        if x - i not in p:
            print(x - i)
            return
        elif x + i not in p:
            print(x + i)
            return

solution()

=======
Suggestion 10

def find_nearest_number(x, p_list):
    if x not in p_list:
        return x
    else:
        return find_nearest_number(x+1, p_list)

x, n = map(int, input().split())
p_list = list(map(int, input().split()))

print(find_nearest_number(x, p_list))
