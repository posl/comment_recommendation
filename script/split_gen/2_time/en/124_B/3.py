def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 1
    max = h[0]
    for i in range(1, n):
        if h[i] >= max:
            count += 1
            max = h[i]
    print(count)
