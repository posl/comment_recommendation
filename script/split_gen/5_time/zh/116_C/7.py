def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    count = 0
    for i in range(1,N+2):
        if h[i] > h[i-1]:
            count += h[i] - h[i-1]
    print(count)
