def main():
    import sys
    from math import sqrt
    input = sys.stdin.readline
    A, B = map(int, input().split())
    g = 1
    time = 0
    while True:
        if time >= A / sqrt(g):
            break
        g += 1
        time += B
    print(time - B)
