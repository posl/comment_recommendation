def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = n+1
    count = 0
    for i in range(n):
        if min > p[i]:
            min = p[i]
            count += 1
    print(count)
