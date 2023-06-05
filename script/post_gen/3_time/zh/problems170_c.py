Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,n = input().split()
    p = input().split()
    x = int(x)
    n = int(n)
    p = list(map(int,p))
    if n == 0:
        print(x)
        return

    p.append(x)
    p.sort()
    index = p.index(x)
    if index == 0:
        print(p[1])
    elif index == len(p)-1:
        print(p[-2])
    else:
        if p[index]-p[index-1] <= p[index+1]-p[index]:
            print(p[index-1])
        else:
            print(p[index+1])

=======
Suggestion 2

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
    for i in range(1,101):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return

=======
Suggestion 3

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    if n == 0:
        print(x)
    else:
        for i in range(1,100):
            if x-i not in p:
                print(x-i)
                break
            elif x+i not in p:
                print(x+i)
                break

=======
Suggestion 4

def getClosestNum(x, p):
    if len(p) == 0:
        return x
    else:
        minNum = 100
        for i in range(0, len(p)):
            if abs(x - p[i]) < minNum:
                minNum = abs(x - p[i])
                result = p[i]
        return result

=======
Suggestion 5

def find_nearest_num(x, p):
    if p == []:
        return x
    else:
        p.sort()
        for i in range(len(p)):
            if x < p[i]:
                return x
            elif x == p[i]:
                return x
            else:
                if i < len(p) -1:
                    if x < (p[i] + p[i+1])/2:
                        return p[i]
                else:
                    return p[i]

=======
Suggestion 6

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    if n == 0:
        print(x)
        return
    if n == 1:
        if p[0] == x:
            print(x+1)
        else:
            print(x)
        return
    if x not in p:
        print(x)
        return
    for i in range(1,x):
        if i not in p:
            print(i)
            return
    print(x+1)

=======
Suggestion 7

def getClosestNumber(x, p):
    p.sort()
    #print(p)
    if x in p:
        return x
    if x < p[0]:
        return p[0]
    if x > p[-1]:
        return p[-1]
    for i in range(len(p)-1):
        if x > p[i] and x < p[i+1]:
            return p[i] if abs(p[i]-x) < abs(p[i+1]-x) else p[i+1]

=======
Suggestion 8

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
        return
    else:
        for i in range(0,101):
            if i not in p:
                if abs(x-i) < abs(x-p[0]):
                    print(i)
                    return
                elif abs(x-i) == abs(x-p[0]) and i < p[0]:
                    print(i)
                    return
        print(p[0])
        return

=======
Suggestion 9

def find_nearest(x, p):
    if len(p) == 0:
        return x
    else:
        p.append(x)
        p.sort()
        i = p.index(x)
        if i == 0:
            return p[1]
        elif i == len(p) - 1:
            return p[len(p) - 2]
        else:
            return p[i + 1] if x - p[i - 1] > p[i + 1] - x else p[i - 1]
