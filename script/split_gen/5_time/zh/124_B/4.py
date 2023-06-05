def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if h[i] >= max:
            count += 1
            max = h[i]
    print(count)
