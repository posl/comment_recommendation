def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if max <= h[i]:
            count += 1
            max = h[i]
    print(count)
