def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] > h[i-1]:
            h[i] -= 1
    for i in range(1, n):
        if h[i] < h[i-1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()