def main():
    n = int(input())
    h = list(map(int, input().split()))
    p = h[0]
    for i in range(1, n):
        if h[i] > p:
            p = h[i]
    print(p)
