def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = p[0]
    for i in range(0, n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)
