def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif h[i] >= max(h[0:i]):
            count += 1
    print(count)
