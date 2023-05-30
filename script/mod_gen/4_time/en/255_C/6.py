def solution():
    # This is the main function
    # Write your code here
    #import sys
    #input = sys.stdin.readline
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if n == 3:
        if a+d == a+2*d:
            print(1)
            return
        else:
            print(2)
            return
    if d > 0:
        if x < a:
            print(2)
            return
        if x == a:
            print(1)
            return
        if x > a:
            if x < a+(n-1)*d:
                print(2)
                return
            if x == a+(n-1)*d:
                print(1)
                return
            if x > a+(n-1)*d:
                print(2)
                return
    if d < 0:
        if x > a:
            print(2)
            return
        if x == a:
            print(1)
            return
        if x < a:
            if x > a+(n-1)*d:
                print(2)
                return
            if x == a+(n-1)*d:
                print(1)
                return
            if x < a+(n-1)*d:
                print(2)
                return
solution()
