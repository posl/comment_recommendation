def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    for i in range(n-1):
        if h[i+1] < h[i]:
            h[i+1] += 1
    for i in range(n-1):
        if h[i+1] < h[i]:
            print('No')
            return
    print('Yes')
