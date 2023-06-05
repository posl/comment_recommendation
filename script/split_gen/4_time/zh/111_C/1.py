def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # print(n)
    count = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 != 0:
                count += 1
        else:
            if a[i] % 2 == 0:
                count += 1
    print(count)
