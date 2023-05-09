def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max_h = h[0]
    for i in range(1, n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)
