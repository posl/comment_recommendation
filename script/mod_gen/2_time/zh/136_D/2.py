def main():
    #n = 5
    #h = [1, 2, 1, 1, 3]
    #n = 4
    #h = [1, 3, 2, 1]
    #n = 5
    #h = [1, 2, 3, 4, 5]
    #n = 1
    #h = [1000000000]
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            h[i + 1] = h[i + 1] - 1
        if h[i] < h[i + 1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()