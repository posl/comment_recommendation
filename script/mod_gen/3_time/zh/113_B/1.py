def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 1000000000
    index = 0
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(temp - a) < min:
            min = abs(temp - a)
            index = i + 1
    print(index)

if __name__ == '__main__':
    main()