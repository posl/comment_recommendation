def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0,0)
    h.append(0)
    result = 0
    for i in range(1,N+1):
        if h[i] > h[i-1] and h[i] > h[i+1]:
            result += 1
    print(result)
