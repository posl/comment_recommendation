def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
            count += 1
    print(count)
