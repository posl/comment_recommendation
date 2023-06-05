def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = 0
    count = 0
    for i in range(n):
        if p[i] > min:
            count += 1
        min = p[i] if p[i] < min or min == 0 else min
    print(count)

if __name__ == '__main__':
    main()