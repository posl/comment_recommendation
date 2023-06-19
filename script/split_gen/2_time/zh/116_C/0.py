def main():
    N = int(input())
    h = [int(i) for i in input().split()]
    h.insert(0,0)
    h.append(0)
    count = 0
    for i in range(1,N+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            count += 1
        elif h[i-1] > h[i] and h[i] < h[i+1]:
            count += 1
    print(count)
