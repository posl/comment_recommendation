def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    count = 0
    for i in range(N):
        if h[i] < h[i+1]:
            count += h[i+1] - h[i]
    print(count)
