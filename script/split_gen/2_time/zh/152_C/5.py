def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 1
    min = p[0]
    for i in range(1, n):
        if p[i] <= min:
            min = p[i]
            count += 1
    print(count)
