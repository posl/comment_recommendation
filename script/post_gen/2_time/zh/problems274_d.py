Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, x, y = map(int, input().split())
    A = list(map(int, input().s

=======
Suggestion 2

def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,x,y)
    #print(a)
    for i in range(n):
        for j in range(i+1,n):
            if i!=j:
                if (x-a[i])**2+(y-a[j])**2 == a[i]**2+a[j]**2:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 3

def is90(x1, y1, x2, y2, x3, y3):
    x1 = x1 - x2
    y1 = y1 - y2
    x3 = x3 - x2
    y3 = y3 - y2
    if x1*x3 + y1*y3 == 0:
        return True
    else:
        return False

=======
Suggestion 4

def is_90degree(x1,y1,x2,y2,x3,y3):
    if (x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)==0:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(abs(x))
    a.append(abs(y))
    a.sort()
    a.reverse()
    if a[0] == a[1]:
        print("No")
    else:
        for i in range(1,n+1):
            if a[i-1] == a[i]:
                print("No")
                break
        else:
            print("Yes")

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))

    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j] == abs(x-y):
                print("Yes")
                exit()
    print("No")

=======
Suggestion 8

def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(0)
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 2):
                if (a[i] - a[j]) * (a[j] - a[k]) == 0 and (a[i] - a[j]) + (a[j] - a[k]) == 0:
                    print("Yes")
                    return
    print("No")

solve()

=======
Suggestion 9

def is_right_angle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
