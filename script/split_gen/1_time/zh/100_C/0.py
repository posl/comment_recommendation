def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while True:
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
                count += 1
            else:
                break
    print(count)
