def main():
    N = int(input())
    balls = [int(x) for x in input().split()]
    count = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        count[balls[i]] += 1
    for i in range(1, 2 * 10 ** 5 + 1):
        count[i] += count[i - 1]
    for i in range(N):
        print(count[balls[i] - 1])

if __name__ == '__main__':
    main()