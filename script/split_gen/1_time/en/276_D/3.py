def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all(x == a[0] for x in a):
            break
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] = a[i] // 3
                count += 1
                break
            elif a[i] % 2 == 0:
                a[i] = a[i] // 2
                count += 1
                break
        else:
            count = -1
            break
    print(count)
