def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, p)
    # print(a)
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)
