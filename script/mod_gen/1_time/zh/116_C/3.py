def get_min_watering_times():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    count = 0
    for i in range(1, N+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            count += 1
    return count

if __name__ == '__main__':
    get_min_watering_times()