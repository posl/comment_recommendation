def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = h[0]
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)
