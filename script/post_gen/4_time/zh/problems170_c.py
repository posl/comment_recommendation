Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

main()

=======
Suggestion 2

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return

    p = list(map(int, input().split()))
    p.sort()

    if x not in p:
        print(x)
        return

    i = 0
    while True:
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return
        i += 1

=======
Suggestion 3

def get_x(n, x, p):
    if n == 0:
        return x
    else:
        p.sort()
        if x in p:
            return get_x(n, x-1, p)
        else:
            for i in range(1, x):
                if x - i in p:
                    return x - i
                elif x + i in p:
                    return x + i

=======
Suggestion 4

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p_list = list(map(int, input().split()))
    p_list.sort()
    if x not in p_list:
        print(x)
        return
    for i in range(1, 101):
        if x - i not in p_list:
            print(x - i)
            return
        elif x + i not in p_list:
            print(x + i)
            return
    return

=======
Suggestion 5

def get_input():
    input_str = raw_input()
    input_list = input_str.split(" ")
    input_list = [int(i) for i in input_list]
    return input_list

=======
Suggestion 6

def get_input():
    x = int(input().strip())
    n = int(input().strip())
    p = []
    if n > 0:
        p = [int(i) for i in input().strip().split()]
    return x, n, p

=======
Suggestion 7

def getClosestNum(x, p):
    #print("x", x)
    #print("p", p)
    if len(p) == 0:
        return x
    minDiff = abs(x-p[0])
    minNum = p[0]
    for i in range(1, len(p)):
        diff = abs(x-p[i])
        if diff < minDiff:
            minDiff = diff
            minNum = p[i]
    return minNum

=======
Suggestion 8

def main():
    #input
    x,n = map(int,input().split())
    p_list = list(map(int,input().split()))

    #process
    if n == 0:
        print(x)
    else:
        p_list.sort()
        for i in range(0,100):
            if x - i not in p_list:
                print(x - i)
                break
            elif x + i not in p_list:
                print(x + i)
                break

=======
Suggestion 9

def main():
    X = int(input("请输入一个整数X："))
    N = int(input("请输入一个整数N："))
    p = [int(i) for i in input("请输入一个长度为N的整数序列：").split()]
    p.append(X)
    p.sort()
    for i in range(len(p)):
        if p[i] == X:
            if i == 0:
                print(p[i+1])
            elif i == len(p)-1:
                print(p[i-1])
            else:
                print(min(p[i-1],p[i+1]))
            break

=======
Suggestion 10

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

    for i in range(x):
        if x - i not in p:
            print(x - i)
            return

        if x + i not in p:
            print(x + i)
            return
