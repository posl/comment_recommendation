def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i%360 for i in a]
    max = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += a[(i+j)%n]
            if sum > max:
                max = sum
    print(max)

if __name__ == '__main__':
    main()