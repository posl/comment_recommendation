def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    total = 0
    for a in A:
        if a > 10:
            total += a - 10
    print(total)
