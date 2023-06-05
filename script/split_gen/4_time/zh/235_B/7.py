def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(n):
        if max_h <= h[i]:
            max_h = h[i]
    print(max_h)
