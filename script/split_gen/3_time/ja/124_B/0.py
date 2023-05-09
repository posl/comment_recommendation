def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if max(h[:i]) <= h[i]:
            count += 1
    print(count)
