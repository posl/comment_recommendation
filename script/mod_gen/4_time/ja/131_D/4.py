def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for j in jobs:
        time += j[1]
        if time > j[0]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()