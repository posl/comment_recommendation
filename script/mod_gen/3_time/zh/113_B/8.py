def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    t -= a
    min = 100000000
    index = 0
    for i in range(n):
        if abs(t-h[i]*0.006) < min:
            min = abs(t-h[i]*0.006)
            index = i+1
    print(index)

if __name__ == '__main__':
    main()