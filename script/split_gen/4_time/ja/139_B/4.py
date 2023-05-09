def solve():
    #n = int(input())
    #a, b = map(int, input().split())
    a, b = map(int, input().split())
    #s = input()
    #a = list(map(int, input().split()))
    #b = [input() for _ in range(n)]
    #print(a, b)
    if b == 1:
        print(0)
        return
    n = b - a
    if n < 0:
        print(0)
        return
    print(n + 1)
