def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            if h[i] - h[i+1] == 1:
                h[i] -= 1
            else:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()