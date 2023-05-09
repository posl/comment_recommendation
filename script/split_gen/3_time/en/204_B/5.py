def main():
    N = int(raw_input())
    A = map(int, raw_input().split())
    sum = 0
    for a in A:
        if a > 10:
            sum += a - 10
    print sum
