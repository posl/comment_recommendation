def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_height = 0
    for i in range(n):
        if h[i] >= max_height:
            max_height = h[i]
            count += 1
    print(count)
