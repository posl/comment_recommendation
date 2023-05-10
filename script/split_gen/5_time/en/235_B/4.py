def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            count += 1
            if count > max_h:
                max_h = count
        else:
            count = 0
    print(max_h)
