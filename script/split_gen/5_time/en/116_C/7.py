def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    #print(N)
    #print(h)
    count = 0
    for i in range(1, N+1):
        if h[i] > h[i-1]:
            count += (h[i] - h[i-1])
        elif h[i] < h[i-1]:
            count += (h[i-1] - h[i])
        else:
            pass
    print(count)
