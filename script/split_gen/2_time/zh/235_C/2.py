def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    maxh = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            maxh = h[i+1]
    print(maxh)
