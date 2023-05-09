def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1])
    time = 0
    for a, b in jobs:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()