def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            count += 1
    print(count)
