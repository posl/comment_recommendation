def main():
    # Get input
    n = int(input())
    h = list(map(int, input().split()))
    # Initialize
    res = True
    h_max = h[0]
    # Loop
    for i in range(1, n):
        if h[i] >= h_max:
            h_max = h[i]
        elif h[i] == h_max - 1:
            h_max = h[i]
        else:
            res = False
            break
    # Output
    if res:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()