def main():
    N = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += h[i]
        else:
            if h[i] > h[i - 1]:
                count += h[i] - h[i - 1]
    print(count)
