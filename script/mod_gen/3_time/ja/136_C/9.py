def main():
    n = int(input())
    h = list(map(int, input().split()))
    if n == 1:
        print('Yes')
        return
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()