def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_height = 0
    for h in H:
        if max_height <= h:
            count += 1
        max_height = max(max_height, h)
    print(count)
