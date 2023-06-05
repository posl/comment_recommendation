def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(n-1):
        if h[i] < h[i+1]:
            h[i+1] -= 1
        if h[i] < h[i+1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()