def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(1, n):
        if h[i] > h[i-1]:
            h[i] -= 1
    for i in range(1, n):
        if h[i] < h[i-1]:
            print('No')
            return
    print('Yes')
    return
main()
