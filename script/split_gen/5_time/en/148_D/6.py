def main():
    N = int(input())
    a = list(map(int, input().split()))
    if 1 not in a:
        print(-1)
    else:
        count = 0
        for i in range(N):
            if a[i] == count + 1:
                count += 1
        print(N - count)
