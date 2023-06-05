def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] == 2:
            count += 1
        else:
            count -= 1
        print(N - count)
