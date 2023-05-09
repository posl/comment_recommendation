def main():
    #input
    n = int(input())
    h = list(map(int, input().split()))
    #process
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
    #output
    print(h.index(max) + 1)

if __name__ == '__main__':
    main()