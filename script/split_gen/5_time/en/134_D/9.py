def solve():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    # Check if a good set of choices exists
    # If a good set of choices exists, print one such set of choices
    # If a good set of choices does not exist, print -1
    # If there is no 1, then the answer is -1
    if 1 not in a:
        print(-1)
        return
    # If there is no 0, then the answer is 0
    if 0 not in a:
        print(0)
        return
    # If there is 1 and 0, then the answer is 1
    print(1)
    print(1)
    return
