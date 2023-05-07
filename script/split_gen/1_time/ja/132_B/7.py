def main():
    n = int(input())
    p = list(map(int, input().split()))
    #print(n, p)
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1]:
            count += 1
        elif p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)
