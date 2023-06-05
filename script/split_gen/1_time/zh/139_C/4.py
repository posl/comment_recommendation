def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
