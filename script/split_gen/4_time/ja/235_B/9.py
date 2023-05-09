def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    #print(h)
    for i in range(n-1):
        if h[i+1] > h[i]:
            h[i+1] -= 1
    h.reverse()
    print(h[0])
