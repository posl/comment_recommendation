def attack(a, b):
    if a > b:
        return a - b
    else:
        return b - a
N = int(input())
A = list(map(int, input().split()))
