def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
    else:
        if a[0] == 1:
            count = 0
            for i in range(1, N):
                if a[i] == a[i-1] + 1:
                    count += 1
                else:
                    break
            print(N - count - 1)
        else:
            print(-1)
