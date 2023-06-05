def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(a - temp) < min:
            min = abs(a - temp)
            index = i
    print(index + 1)

if __name__ == '__main__':
    main()