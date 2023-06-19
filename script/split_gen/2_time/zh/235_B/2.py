def main():
    n = int(input())
    h = list(map(int, input().split()))
    current_h = h[0]
    for i in range(1, n):
        if h[i] > current_h:
            current_h = h[i]
    print(current_h)
