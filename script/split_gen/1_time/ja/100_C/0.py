def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                print(count)
                return
        count += 1
