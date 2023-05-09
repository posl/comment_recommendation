def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(1)
        return
    a.sort()
    count = 0
    for i in range(N):
        if a[i] <= i+1:
            count = i+1
    print(count)
