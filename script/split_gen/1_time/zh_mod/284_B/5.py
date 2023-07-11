def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for a in A:
        if a % 2 != 0:
