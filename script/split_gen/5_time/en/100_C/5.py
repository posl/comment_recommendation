def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        c = 0
        while a[i] % 2 == 0:
            a[i] /= 2
            c += 1
        count += c
    print(count)
