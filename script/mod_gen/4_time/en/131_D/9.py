def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1])
    current_time = 0
    for a, b in jobs:
        current_time += a
        if current_time > b:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()